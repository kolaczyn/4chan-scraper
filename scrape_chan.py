import os
import sys

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup


def fetch_page(url):
    try:
        return requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        print('Exiting')
        exit(1)


def make_dir(dir_name):
    curr_dir = os.getcwd()
    path = os.path.join(curr_dir, dir_name)
    os.makedirs(path, exist_ok=True)


def figure_out_folder_name(soup):
    subject = soup.find('span', {'class': 'subject'}).text
    message = soup.find('blockquote', {'class': 'postMessage'}).text[:15]
    # short circuit - return first letters of the post, if there is no subject
    return subject or message


def fetch_and_save_file(url, label, directory):
    file_data = requests.get(url).content
    file_name = os.path.join('threads', directory, label)
    with open(file_name, 'wb') as handler:
        handler.write(file_data)


def scrape_files(thread_link):
    website_html = fetch_page(thread_link).text
    soup = BeautifulSoup(website_html, 'html.parser')

    folder_name = figure_out_folder_name(soup)

    make_dir('threads')
    make_dir(os.path.join('threads', folder_name))

    file_elems = (soup.find_all('div', {'class': 'fileText'}))
    for file_elem in tqdm(file_elems):
        anchor = file_elem.find('a')
        url = f'http:{anchor.attrs["href"]}'
        fetch_and_save_file(url, anchor.string, folder_name)


if __name__ == '__main__':
    thread_link = sys.argv[1]
    scrape_files(thread_link)
