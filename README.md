# twarc-videos

This twarc plugin uses [youtube_dl] to download videos and their metadata from
tweets. This is nice because youtube_dl downloads video from [many more
platforms] than YouTube including Twitter itself.

To use twarc-videos first you need to install twarc and this plugin:

    pip install twarc
    pip install twarc-videos

Now you can collect data using the core twarc utility, for example:

    twarc2 search 'nirvana (has:videos OR url:"https://youtu.be")' > nirvana-tweets.jsonl

And you have a new subcommand `videos` that is supplied by twarc-videos.

    twarc2 videos nirvana-tweets.jsonl

Once it is finished you will have a new `videos` directory that looks something
like:

```
videos
├── archive.txt
├── mapping.tsv
├── twitter
│   ├── 1339223561731530753
│   │   ├── Psychedelia_-_Nirvana_-_Come_As_You_Are.description
│   │   ├── Psychedelia_-_Nirvana_-_Come_As_You_Are.info.json
│   │   └── Psychedelia_-_Nirvana_-_Come_As_You_Are.mp4
│   ├── 1341668409428353025
│   │   ├── Rt_Your_Fav_Bands_-_Nirvana_Come_As_You_Are.description
│   │   ├── Rt_Your_Fav_Bands_-_Nirvana_Come_As_You_Are.info.json
│   │   └── Rt_Your_Fav_Bands_-_Nirvana_Come_As_You_Are.mp4
│   ├── 1374212180002926594
│   │   ├── Hanna_-_She_s_in_Nirvana....description
│   │   ├── Hanna_-_She_s_in_Nirvana....info.json
│   │   └── Hanna_-_She_s_in_Nirvana....mp4
│   ├── 1374467789885378569
│   │   ├── MUSIC_NOSTALGIA_-_Nirvana_The_Man_Who_Sold_The_World_..description
│   │   ├── MUSIC_NOSTALGIA_-_Nirvana_The_Man_Who_Sold_The_World_..info.json
│   │   └── MUSIC_NOSTALGIA_-_Nirvana_The_Man_Who_Sold_The_World_..mp4
│   ├── 1374469206226264067
│   │   ├── Take_it_easy_-_Abuelo_donde_andas_Nirvana.description
│   │   ├── Take_it_easy_-_Abuelo_donde_andas_Nirvana.info.json
│   │   └── Take_it_easy_-_Abuelo_donde_andas_Nirvana.mp4
│   ├── 1374631023502360576
│   │   ├── OraEtLabora_-_Reel_Stories_-_Dave_Grohl_is_on_@bbctwo_this_Saturday_at_10.30pm...talking_@Nirvana_amp_@foofighters_with_Dermot_@radioleary_@wearecraftuk.description
│   │   ├── OraEtLabora_-_Reel_Stories_-_Dave_Grohl_is_on_@bbctwo_this_Saturday_at_10.30pm...talking_@Nirvana_amp_@foofighters_with_Dermot_@radioleary_@wearecraftuk.info.json
│   │   └── OraEtLabora_-_Reel_Stories_-_Dave_Grohl_is_on_@bbctwo_this_Saturday_at_10.30pm...talking_@Nirvana_amp_@foofighters_with_Dermot_@radioleary_@wearecraftuk.mp4
│   ├── 1374656171844329477
│   ├── 1374656880694292483
│   ├── 1374660019241762817
│   ├── 1374664809078272000
│   └── 1374671562016661506
│       ├── John_-_Nirvana_-_In_Bloom_Live_at_Reading_1992_@YouTube.description
│       ├── John_-_Nirvana_-_In_Bloom_Live_at_Reading_1992_@YouTube.info.json
│       └── John_-_Nirvana_-_In_Bloom_Live_at_Reading_1992_@YouTube.mp4
└── youtube
    ├── 5X9CGFQyjN4
    │   ├── Heart-Shaped_Box_Nirvana_Music_Box.description
    │   ├── Heart-Shaped_Box_Nirvana_Music_Box.en.vtt
    │   ├── Heart-Shaped_Box_Nirvana_Music_Box.info.json
    │   └── Heart-Shaped_Box_Nirvana_Music_Box.mp4
    ├── AhcttcXcRYY
    │   ├── Nirvana_-_About_A_Girl_MTV_Unplugged.description
    │   ├── Nirvana_-_About_A_Girl_MTV_Unplugged.en.vtt
    │   ├── Nirvana_-_About_A_Girl_MTV_Unplugged.info.json
    │   └── Nirvana_-_About_A_Girl_MTV_Unplugged.mp4
    ├── AXU-LaaO_xQ
    │   ├── Nirvana_Drain_You_lyrics_sub_espanol.description
    │   ├── Nirvana_Drain_You_lyrics_sub_espanol.info.json
    │   └── Nirvana_Drain_You_lyrics_sub_espanol.mp4
    ├── D742dNm1f8Q
    │   ├── Nirvana_-_In_Bloom_Live_at_Reading_1992.description
    │   ├── Nirvana_-_In_Bloom_Live_at_Reading_1992.info.json
    │   └── Nirvana_-_In_Bloom_Live_at_Reading_1992.mp4
    ├── -fh-bqSV73E
    │   ├── Becoming_a_minimalist_w_Matt_D_Avella.description
    │   ├── Becoming_a_minimalist_w_Matt_D_Avella.en.vtt
    │   ├── Becoming_a_minimalist_w_Matt_D_Avella.info.json
    │   └── Becoming_a_minimalist_w_Matt_D_Avella.mp4
    ├── hTWKbfoikeg
    │   ├── Nirvana_-_Smells_Like_Teen_Spirit_Official_Music_Video.description
    │   ├── Nirvana_-_Smells_Like_Teen_Spirit_Official_Music_Video.en.vtt
    │   ├── Nirvana_-_Smells_Like_Teen_Spirit_Official_Music_Video.info.json
    │   └── Nirvana_-_Smells_Like_Teen_Spirit_Official_Music_Video.mp4
    ├── jWkSt4G8F18
    │   ├── Nirvana_healing_centre_overview.description
    │   ├── Nirvana_healing_centre_overview.info.json
    │   └── Nirvana_healing_centre_overview.mp4
    ├── MW6E_TNgCsY
    │   ├── Everclear_-_Santa_Monica_Official_Music_Video.description
    │   ├── Everclear_-_Santa_Monica_Official_Music_Video.info.json
    │   └── Everclear_-_Santa_Monica_Official_Music_Video.mp4
    ├── n6P0SitRwy8
    │   ├── Nirvana_-_Heart-Shaped_Box.description
    │   ├── Nirvana_-_Heart-Shaped_Box.info.json
    │   └── Nirvana_-_Heart-Shaped_Box.mp4
    ├── OgeR2oqZGTs
    │   ├── Nirvana_-_The_Man_Who_Sold_The_World_Live_On_MTV_Unplugged_1993_Unedited.description
    │   ├── Nirvana_-_The_Man_Who_Sold_The_World_Live_On_MTV_Unplugged_1993_Unedited.en.vtt
    │   ├── Nirvana_-_The_Man_Who_Sold_The_World_Live_On_MTV_Unplugged_1993_Unedited.info.json
    │   └── Nirvana_-_The_Man_Who_Sold_The_World_Live_On_MTV_Unplugged_1993_Unedited.mp4
    ├── v9RY25eImcw
    │   ├── Nirvana_-_Smells_Like_Teen_Spirit_Cover_RADIO_TAPOK.description
    │   ├── Nirvana_-_Smells_Like_Teen_Spirit_Cover_RADIO_TAPOK.en.vtt
    │   ├── Nirvana_-_Smells_Like_Teen_Spirit_Cover_RADIO_TAPOK.info.json
    │   └── Nirvana_-_Smells_Like_Teen_Spirit_Cover_RADIO_TAPOK.mp4
    ├── ycHvL3W3_PA
    │   ├── Nirvana_-_Where_Did_You_Sleep_Last_Night_8D_Audio.description
    │   ├── Nirvana_-_Where_Did_You_Sleep_Last_Night_8D_Audio.info.json
    │   └── Nirvana_-_Where_Did_You_Sleep_Last_Night_8D_Audio.mp4
    └── y-lQgqHD8Xs
        ├── dodo_tofubeats_-_nirvana_Official_Music_Video.description
        ├── dodo_tofubeats_-_nirvana_Official_Music_Video.info.json
        └── dodo_tofubeats_-_nirvana_Official_Music_Video.mp4
```

The `video/mapping.tsv` file is a tab separated value file of video URLs found
and their corresponding location in disk. 

## Testing

To run the tests you will need create a `.env` file that looks like:

    BEARER_TOKEN=YOUR_TOKEN_HERE

And then:

    python setup.py test

[twarc]: https://github.com/docnow/twarc 
[youtube_dl]: https://youtube-dl.org/ 
[more platforms]: http://ytdl-org.github.io/youtube-dl/supportedsites.html

