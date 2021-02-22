import os
import sys

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup


def fetch_and_save_file(url, label, directory):
    file_data = requests.get(url).content
    file_name = os.path.join('threads', directory, label)
    with open(file_name, 'wb') as handler:
        handler.write(file_data)


def make_dir(dir_name):
    curr_dir = os.getcwd()
    path = os.path.join(curr_dir, dir_name)
    try:
        os.mkdir(path)
    except FileExistsError:
        print('Folder already exists.')


def fetch_page(url):
    try:
        return requests.get(url)
    except Exception as ex:
        print(f'{ex}')
        exit(1)


def figure_out_folder_name(soup):
    subject = soup.find('span', {'class': 'subject'}).text
    message = soup.find('blockquote', {'class': 'postMessage'}).text[:15]
    # short circuit - return first letters of the post, if there is no subject
    return subject or message


def scrape_files():
    thread_link = sys.argv[1]

    data = fetch_page(thread_link)

    soup = BeautifulSoup(data.text, 'html.parser')

    folder_name = figure_out_folder_name(soup)

    make_dir('threads')
    make_dir(os.path.join('threads', folder_name))
    # make_dir(('threads', file_name))

    file_elems = (soup.find_all('div', {'class': 'fileText'}))
    for file_elem in tqdm(file_elems):
        anchor = file_elem.find('a')
        # url has a weird formatting
        url = f'http:{anchor.attrs["href"]}'
        print(url, anchor.string, folder_name)
        fetch_and_save_file(url, anchor.string, folder_name)


def save_to_csv():
    pass


scrape_files()
