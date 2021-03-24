import os
import json
import dotenv
import shutil
import pathlib
import twarc_videos

from twarc.client2 import Twarc2
from click.testing import CliRunner

dotenv.load_dotenv()
bearer_token = os.environ.get('BEARER_TOKEN')
test_data = pathlib.Path('test.json')
test_videos_dir = pathlib.Path('videos')

if test_videos_dir.is_dir():
    shutil.rmtree(test_videos_dir)

def test_bearer_token():
    assert bearer_token

def test_get_youtube_tweet():
    if test_data.is_file():
        test_data.unlink()
    t = Twarc2(bearer_token=bearer_token)
    results = next(t.search_recent('url:"https://youtu.be"'))
    results['data'] = results['data'][0:2]
    json.dump(results, test_data.open('w'))

def test_download_youtube():
    assert test_data.is_file()
    runner = CliRunner()
    result = runner.invoke(twarc_videos.videos, ['--timeout', 10, 'test.json'])
    assert test_videos_dir.is_dir()
    videos_dir = test_videos_dir / "youtube"
    assert videos_dir.is_dir()
    assert len(list(videos_dir.iterdir())) > 0

def test_get_vimeo_tweet():
    if test_data.is_file():
        test_data.unlink()
    t = Twarc2(bearer_token=bearer_token)
    results = next(t.search_recent('url:"https://vimeo.com"'))
    results['data'] = results['data'][0:2]
    json.dump(results, test_data.open('w'))

def test_download_vimeo():
    assert test_data.is_file()
    runner = CliRunner()
    result = runner.invoke(twarc_videos.videos, ['--timeout', 10, 'test.json'])
    assert test_videos_dir.is_dir()
    videos_dir1 = test_videos_dir / "vimeo"
    videos_dir2 = test_videos_dir / "vimeo_-ondemand"
    assert videos_dir1.is_dir() or videos_dir2.is_dir()
    assert len(list(videos_dir1.iterdir())) > 0 or len(list(videos_dir2.iterdir())) > 0


