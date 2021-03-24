# twarc-videos

This twarc plugin uses [youtube_dl] to download videos and their metadata from
tweets. youtube_dl downloads video from [more platforms] than youtube.

First you need to install twarc and this plugin:

    pip install twarc
    pip install twarc-videos

Now you can collect data using the core twarc utility:

    twarc2 search blacklivesmatter > tweets.jsonl

And you have a new subcommand `videos` that is supplied by twarc-videos.

    twarc2 videos tweets.jsonl

Once it is finished you will have a new directory with the following structure:

```
videos
├── archive.txt
├── mapping.tsv
├── twitter
│   ├── 1374300739112206341
│   │   ├── andrea_s_bts_BE_-_COWAY_X_BTS_BTS_@BTS_twt.description
│   │   ├── andrea_s_bts_BE_-_COWAY_X_BTS_BTS_@BTS_twt.info.json
│   │   └── andrea_s_bts_BE_-_COWAY_X_BTS_BTS_@BTS_twt.mp4
│   └── 1374513136145891334
│       ├── BTS_X_60_BTS_@BTS_twt.description
│       ├── BTS_X_60_BTS_@BTS_twt.info.json
│       └── BTS_X_60_BTS_@BTS_twt.mp4
└── youtube
    ├── 1K7d_pE76QA
    │   ├── _.description
    │   ├── _.info.json
    │   └── _.mp4
    ├── 3A-2QM1ULTw
    │   ├── Japanese_Hokkaido_Hero_Sohrandragon_Short_Film_PV_PV.description
    │   ├── Japanese_Hokkaido_Hero_Sohrandragon_Short_Film_PV_PV.en.vtt
    │   ├── Japanese_Hokkaido_Hero_Sohrandragon_Short_Film_PV_PV.info.json
    │   └── Japanese_Hokkaido_Hero_Sohrandragon_Short_Film_PV_PV.mp4
    ├── DaXS0SbjXwQ
    │   ├── COWAY_X_BTS.description
    │   ├── COWAY_X_BTS.en.vtt
    │   ├── COWAY_X_BTS.info.json
    │   └── COWAY_X_BTS.mp4
    ├── ddzYSkX8080
    │   ├── INTERVENCAO_JA_CENAS_DE_TERROR_PELO_BRASIL_-_POLICIAIS_COVARDES_MASSACRAM_O_PROPRIO_POVO_2021-03-23_21_47.description
    │   ├── INTERVENCAO_JA_CENAS_DE_TERROR_PELO_BRASIL_-_POLICIAIS_COVARDES_MASSACRAM_O_PROPRIO_POVO_2021-03-23_21_47.info.json
    │   └── INTERVENCAO_JA_CENAS_DE_TERROR_PELO_BRASIL_-_POLICIAIS_COVARDES_MASSACRAM_O_PROPRIO_POVO_2021-03-23_21_47.mp4.part
    ├── dSkQJD4sJRA
    │   ├── BTS_X_60.description
    │   ├── BTS_X_60.en.vtt
    │   ├── BTS_X_60.info.json
    │   └── BTS_X_60.mp4
    ├── haOys7E2Zbo
    │   ├── Stephen_Lynch_D_D.description
    │   ├── Stephen_Lynch_D_D.en.vtt
    │   ├── Stephen_Lynch_D_D.info.json
    │   └── Stephen_Lynch_D_D.mp4
    ├── IXPsn-yNMgo
    │   ├── _...description
    │   ├── _...en.vtt
    │   ├── _...info.json
    │   └── _...mp4
    ├── MmDZbjI8nHw
    │   ├── I_ve_Got_A_Feeling.description
    │   ├── I_ve_Got_A_Feeling.info.json
    │   └── I_ve_Got_A_Feeling.mp4
    └── Sa-NPuRrnK8
        ├── ~_YOU_QUIZ_ON_THE_BLOCK_EP.99.description
        ├── ~_YOU_QUIZ_ON_THE_BLOCK_EP.99.en.vtt
        ├── ~_YOU_QUIZ_ON_THE_BLOCK_EP.99.info.json
        └── ~_YOU_QUIZ_ON_THE_BLOCK_EP.99.mp4
```

## Testing

To run the tests you will need create a `.env` file that looks like:

    BEARER_TOKEN=YOUR_TOKEN_HERE

[twarc]: https://github.com/docnow/twarc 
[youtube_dl]: https://youtube-dl.org/ 
[more platforms]: http://ytdl-org.github.io/youtube-dl/supportedsites.html

