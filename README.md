# BOTKACA

Botkaca allows you to leech (re-upload) contents from internet including torrent to telegram. This bot using Telegram MTProto powered by pyrogram.

## Feature

* Set as Private (using password)
* Able to use at group
* Able to leech larger than 2GB (telegram max upload at once)
* Split as video (.mp4, .mkv, .avi, .webm, .wmv, .mov)
* Upload files as media or as document
* Upload files as a single zip file
* Custom thumbnail
* Default torrent tracker
* Customizeable language (default is english)
* Configuration using environment variable

## Configuration

Change config by set the corresponding environment variable name.

* `WORKDIR` : working directory path
* `LOG_FILE` : log file name
* `MAX_LOG_SIZE` : maximum log size
* `EDIT_SLEEP` : delay between edit message
* `UPLOAD_MAX_SIZE` : maximum file size (in bytes) upload at once (watchout telegram max upload size)
* `UPLOAD_AS_DOC` : upload any files as document (1 or 0)
* `UPLOAD_AS_ZIP` : upload any files as a bundled zip file (1 or 0)
* `ARIA2_DIR` : download directory before uploading
* `TORRENT_TRACKER` : addition tracker for all torrent, separated by (`,`)
* `BAR_SIZE` : bar size on upload and download
* `THUMBNAIL_NAME` : default thumbnail file name
* `LOCAL` : languange bot using
* `CHAT_ID` : default chat_ids that have access to bot, separated by (`,`)

## Deploy button

[<img src="https://deploy.cloud.run/button.svg" alt="Run on Google Cloud" height="40"/>](https://deploy.cloud.run?git_repo=https://github.com/azamaulanaaa/botkaca.git "Google Cloud")
[<img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" height="40"/>](https://heroku.com/deploy?template=https://github.com/azamaulanaaa/botkaca "Heroku")

*Currently google cloud does not supported due to app.json clash with heroku. Check out Google Cloud Run issue [#112](https://github.com/GoogleCloudPlatform/cloud-run-button/issues/112#issuecomment-663858778 "Both Cloud Run Button and Heroku Button - app.json Clash")*

## How to run

```sh
#!/bin/sh

# get botkaca source
git clone https://github.com/azamaulanaaa/botkaca.git

# build then execute using docker image
docker build -t azamaulanaaa/botkaca botkaca
docker run -it azamaulanaaa/botkaca
```

## Bot Details

### Specification

* Python 3
* Python Library
    * pyrogram asyc
    * tgcrypto
    * aria2p
* Program Dependece
    * aria2c
    * ffmpeg + ffprobe
* Dockerize (multi-stage)

### Folder Structure

* `/` : development detail and deploy config
* `/bot` : module root dir
    * `__init__.py` : bot config
    * `__main__.py` : register handler then run bot
    * `config.py` : create configuration and configurable from env var
* `/bot/handler` : message handler
* `/bot/locals` : localization and default is en
* `/bot/plugins` : third party implementation