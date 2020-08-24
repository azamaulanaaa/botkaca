# BOTKACA

Telegram bot leecher powered by python3.

## Deploy button

~~`[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run?git_repo=https://github.com/azamaulanaaa/botkaca.git "Google Cloud")`~~

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/azamaulanaaa/botkaca "Heroku")

*Currently google cloud does not supported due to app.json clash with heroku. Check out [issue #112](https://github.com/GoogleCloudPlatform/cloud-run-button/issues/112 "Both Cloud Run Button and Heroku Button - app.json Clash")*

## How to run

```sh
#!/bin/sh
git clone https://github.com/azamaulanaaa/botkaca.git
cd botkaca
docker build -t botkaca .
docker run -it botkaca
```
