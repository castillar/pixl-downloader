# pixl-downloader
Simple python downloader for pixl.is albums. Project inspired from [pixl-mass-downloader](https://github.com/dhaouiaziz13/pixl-mass-downloader).

## Installation

```bash
# use bash it don't work well with fish.
$ bash
# copy project file to your computer
$ git clone https://github.com/dix0nym/pixl-downloader.git
# got to the project folder
$ cd pixl-downloader
# create virtualenv if necessary (if you don't have it : sudo apt install python3-virtualenv )
$ virtualenv env
# activiate environment
$ source env/bin/activate
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
