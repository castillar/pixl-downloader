# pixl-downloader
Simple python downloader for pixl.is albums. Project inspired from [pixl-mass-downloader](https://github.com/dhaouiaziz13/pixl-mass-downloader).

## Installation

```bash
# create virtualenv if necessary
$ virualenv env
# activiate environment
$ source env/Scripts/activate
# install needed packages
$ pip install requests bs4
# or using requirements.txt
$ pip install -r requirements.txt
```

## Usage

```bash
$ python downloader.py -h
usage: downloader.py [-h] [-d DESTINATION] URL

downloader for pixl

positional arguments:
  URL                   album url to download images

options:
  -h, --help            show this help message and exit
  -d DESTINATION, --destination DESTINATION
                        destination to store images
```

example call: `$ python downloader.py -d /media/storage/pixl-downloads/ https://pixl.is/album/XXXXXX`
