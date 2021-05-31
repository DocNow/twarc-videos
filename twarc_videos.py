import os
import sys
import json
import time
import click
import logging
import youtube_dl
import multiprocessing as mp

from urllib.parse import urlparse
from twarc import ensure_flattened
from datetime import datetime, timedelta
from youtube_dl.utils import match_filter_func

@click.command()
@click.option('--max-downloads', type=int, help='max downloads per URL')
@click.option('--max-filesize', type=int, help='max filesize to download (bytes)')
@click.option('--ignore-livestreams', is_flag=True, default=False, help='ignore livestreams')
@click.option('--download-dir', type=str, default='videos', help='directory to download to')
@click.option('--block', multiple=True, help='hostname(s) to block (repeatable)')
@click.option('--timeout', type=int, default=120, help='seconds to wait for a video download to finish')
@click.option('--quiet', is_flag=True, default=False, help='silence terminal output')
@click.argument('infile', type=click.File('r'), default='-')
def videos(max_downloads, max_filesize, ignore_livestreams, download_dir, block, timeout, infile, quiet):
    """
    Download videos referenced in tweets and their metadata.
    """

    # make download directory
    download_dir = download_dir
    if not os.path.isdir(download_dir):
        os.mkdir(download_dir)

    # setup logger
    log_file = "{}/twarc-videos.log".format(download_dir)
    logging.basicConfig(filename=log_file, level=logging.INFO)
    log = logging.getLogger()

    # setup youtube_dl config
    ydl_opts = {
        "format": "best",
        "logger": log,
        "restrictfilenames": True,
        "ignoreerrors": True,
        "nooverwrites": True,
        "writedescription": True,
        "writeinfojson": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "outtmpl": "{}/%(extractor)s/%(id)s/%(title)s.%(ext)s".format(download_dir),
        "download_archive": "{}/archive.txt".format(download_dir)
    }
    if ignore_livestreams:
        ydl_opts["matchfilter"] = match_filter_func("!is_live")
    if max_downloads:
        ydl_opts['max_downloads'] = max_downloads
    if max_filesize:
        ydl_opts['max_filesize'] = max_filesize

    # keep track of domains to block
    blocklist = []
    if block:
        blocklist = block

    # read in existing mapping file to know which urls we can ignorej
    seen = set()
    mapping_file = os.path.join(download_dir, 'mapping.tsv')
    if os.path.isfile(mapping_file):
        for line in open(mapping_file):
            url, path = line.split('\t')
            log.info('found %s in %s', url, mapping_file)
            seen.add(url)

    # loop through the tweets
    results = open(mapping_file, 'a')
    for line in infile:
        for tweet in ensure_flattened(json.loads(line)):
            log.info('analyzing %s', tweet['id'])
            for url in video_urls(tweet):
                if url in seen:
                    log.info('already processed %s', url)
                    continue
                seen.add(url)

                # check for blocks
                uri = urlparse(url)
                if uri.netloc in blocklist:
                    logging.warn("%s in block list", url)
                    continue

                log.info('processing %s', url)
   
                manager = mp.Manager()
                return_list = manager.list()

                p = mp.Process(target=download, args=(url, ydl_opts, log, max_downloads, return_list))
                p.start()

                started = datetime.now()
                while True:
                    # if we've exceeded the timeout terminate the process
                    if timeout and datetime.now() - started > timedelta(seconds=timeout):
                        log.warning('reached timeout %s', timeout)
                        p.terminate()
                        break
                    # if the process is done we can stop
                    elif not p.is_alive():
                        break
                    # otherwise sleep and the check again
                    time.sleep(1)

                p.join()

                # if the queue was empty there either wasn't a download or it timed out
                filename = return_list.pop() if len(return_list) > 0 else None

                if not quiet and filename:
                    click.echo(f'downloaded {click.style(url, fg="blue")} as {click.style(filename, fg="green")}')

                # write the result to the mapping file
                results.write("{}\t{}\n".format(url, filename))

def video_urls(t):

    if 'entities' not in t:
        return

    # if video is attached to the tweet return the tweet url
    attachments = t['entities'].get('attachments', {})
    for media in attachments.get('media', []):
        if media['type'] == 'video':
            yield f"https://twitter.com/{t['author']['username']}/status/{t['id']}" 

    # return every url in a tweet to see if video can be extracted
    for url in t['entities'].get('urls', []):
        yield url['expanded_url']


def download(url, ydl_opts, log, max_downloads, return_list):
    try:
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        info = ydl.extract_info(url)
        if info:
            filename = ydl.prepare_filename(info)
            if os.path.isfile(filename):
                return_list.append(filename)
                logging.info('downloaded %s as %s', url, filename)
        else:
            logging.warning("%s doesn't look like a video", url)
    except youtube_dl.utils.MaxDownloadsReached as e:
        logging.warning('only %s downloads per url allowed', max_downloads)


