import argparse
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup as bs


def get_album_name(url):
    if '/' not in url:
        return None
    tmp = url.split('/')[-1]
    if '.' not in tmp or len(tmp) != 2:
        return None
    return tmp.split('.')[0]

def get_next_page(soup):
    links = soup.findAll(attrs={"data-pagination": "next"})
    if links and links[0].has_attr('href'):
        return links[0].attrs['href']
    return None

def get_urls(soup):
    img_container = soup.select('a.image-container')
    thumb_urls = [container.select_one('img')['src'] for container in img_container]
    transformUrl = lambda url: url.replace('.md', '')
    urls = list(map(transformUrl, thumb_urls))
    return urls

def download_images(download_dir, urls):
    while urls:
        url = urls.pop()
        print(f"\t[+] downloading url: {url}")
        filename = f"{url.split('/').pop()}.jpg"
        path = Path.joinpath(download_dir, filename)
        response = requests.get(url)
        if response.status_code != 200:
            print(f"\t[!] failed to download url - retrying in 5s")
            time.sleep(5)
            continue
        with path.open('wb') as f:
            f.write(response.content)
        time.sleep(0.5)

def prepare_output_directory(url, destination):
    album_name = get_album_name(url)
    if album_name:
        output_dir = Path.joinpath(destination, album_name)
    else:
        output_dir = Path.joinpath(destination, f"pixl-download-{int(time.time())}")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir

def start_crawling(url, download_dir):
    while url:
        response = requests.get(url)
        if response.status_code != 200:
            print("request failed => retrying")
            continue
        soup = bs(response.text, 'html.parser')
        urls = get_urls(soup)
        print(f'[+] found {len(urls)} images on current page')
        download_images(download_dir, urls)
        next_page = get_next_page(soup)
        if next_page:
            print(f'[+] found new page url: {next_page}')
        else:
            print(f'[!] no new page => finished downloading!')
        url = next_page

def main():
    parser = argparse.ArgumentParser(description='downloader for pixl')
    parser.add_argument('-d', '--destination', type=str, help='destination to store images', required=False, default="./downloads/")
    parser.add_argument('url', metavar='URL', type=str, help='album url to download images')
    args = parser.parse_args()
    destination = Path(args.destination)
    url = args.url

    output_dir = prepare_output_directory(url, destination)
    start_crawling(url, output_dir)


if __name__ == '__main__':
    main()
