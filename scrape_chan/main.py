import os
import sys

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup


def fetch_page(url: "string"):
    """fetches the page with the request module, exists on any exception"""
    print('Fetching website...')
    try:
        return requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        print('Exiting')
        exit(1)


def make_dir(dir_name: "string"):
    """creates a directory in currect directory"""
    curr_dir = os.getcwd()
    path = os.path.join(curr_dir, dir_name)
    os.makedirs(path, exist_ok=True)


def figure_out_thread_name(soup) -> str:
    """
    Returns the subject of the thread.
    If there is none, it returns the beginning of the thread's first post
    """
    subject = soup.find('span', {'class': 'subject'}).text
    message = soup.find('blockquote', {'class': 'postMessage'}).text[:15]
    # short circuit - return first letters of the post, if there is no subject
    return subject or message


def fetch_and_save_file(url: "string", thread_name: "string", label: "string"):
    """
    Fetches the file from the provided url,
    and saves in folder f'{thread_name}/{label}'
    """
    file_data = requests.get(url).content
    file_name = os.path.join('threads', thread_name, label)
    with open(file_name, 'wb') as handler:
        handler.write(file_data)


def scrape_files(thread_link):
    website_html = fetch_page(thread_link).text
    soup = BeautifulSoup(website_html, 'html.parser')

    thread_name = figure_out_thread_name(soup)

    make_dir('threads')
    make_dir(os.path.join('threads', thread_name))

    # inside div with a class="fileText", there an anchor tag, 
    # which holds the link to the file and the file's name
    file_elems = (soup.find_all('div', {'class': 'fileText'}))
    for file_elem in tqdm(file_elems):
        anchor = file_elem.find('a')
        url = f'http:{anchor.attrs["href"]}'
        fetch_and_save_file(url, thread_name, label=anchor.string)
