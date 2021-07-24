import argparse
import asyncio
import aiohttp

from tqdm import tqdm as bar

from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor
import re
from datasets import Dataset, DatasetDict
import json


parser = argparse.ArgumentParser(description='Process some arguments.')
parser.add_argument('--artist_id', type=int, help='Artist ID in Genius API')
parser.add_argument('--token', type=str, help='Genius API token')
parser.add_argument('--save_path', type=str, help='Path where to save the resulting json file')
args = parser.parse_args()


async def get_song_urls(artist_id):
    access_token = 'Bearer ' + args.token
    authorization_header = {'authorization': access_token}
    urls = []
    async with aiohttp.ClientSession(headers=authorization_header) as session:
        with bar(total=None) as pbar:
            pbar.set_description("⏳ Searching songs...")
            next_page = 1
            while next_page is not None:
                async with session.get(
                        f"https://api.genius.com/artists/{artist_id}/songs?sort=popularity&per_page=50&page={next_page}",
                        timeout=999) as resp:
                    response = await resp.json()
                    response = response['response']
                next_page = response['next_page']

                for song in response['songs']:
                    urls.append(song['url'])
                pbar.update(len(response['songs']))
            # pbar.set_description("✅ Done")
    return urls


def process_page(html):
    '''Meant for CPU-bound workload'''
    html = BeautifulSoup(html.replace('<br/>', '\n'), 'html.parser')
    div = html.find("div", class_=re.compile("^lyrics$|Lyrics__Root"))
    if div is None:
        lyrics = ""
    else:
        lyrics = div.get_text()

    lyrics = re.sub(r'(\[.*?\])*', '', lyrics)
    lyrics = re.sub('\n{2}', '\n', lyrics)  # Gaps between verses

    lyrics = str(lyrics.strip("\n"))
    lyrics = lyrics.replace("EmbedShare URLCopyEmbedCopy", "").replace("'", "")
    lyrics = re.sub("[\(\[].*?[\)\]]", "", lyrics)
    lyrics = re.sub(r'\d+$', '', lyrics)
    lyrics = str(lyrics).lstrip().rstrip()
    lyrics = str(lyrics).replace("\n\n", "\n")
    lyrics = str(lyrics).replace("\n\n", "\n")
    lyrics = re.sub(' +', ' ', lyrics)
    return lyrics


async def fetch_page(url, session):
    '''Meant for IO-bound workload'''
    async with session.get(url, timeout=999) as res:
        return await res.text()


async def process(url, session, pool, pbar):
    html = await fetch_page(url, session)
    pbar.update(1)
    return await asyncio.wrap_future(pool.submit(process_page, html))


async def parse_lyrics(urls):
    pool = ProcessPoolExecutor()
    pbar = bar(total=len(urls))
    async with aiohttp.ClientSession() as session:
        pbar.set_description("⏳ Parsing lyrics...")
        coros = (process(url, session, pool, pbar) for url in urls)
        return await asyncio.gather(*coros)


def create_dataset(lyrics):
  dataset = {}
  dataset['train'] = Dataset.from_dict({'text': list(lyrics)})
  datasets = DatasetDict(dataset)
  del dataset
  return datasets


def save_dataset(datasets):
    train = datasets['train'].to_dict()
    dataset_dict = {'train': train['text']}
    with open(args.save_path, 'w', encoding='utf-8') as fp:
        json.dump(dataset_dict, fp, ensure_ascii=False)


def main():

    loop = asyncio.get_event_loop()
    urls = loop.run_until_complete(get_song_urls(args.artist_id))
    lyrics = loop.run_until_complete(parse_lyrics(urls))
    loop.close()

    dataset = create_dataset(lyrics)
    save_dataset(dataset)


if __name__ == '__main__':
    main()
