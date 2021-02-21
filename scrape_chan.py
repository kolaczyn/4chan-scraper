import os
import sys
import requests
from bs4 import BeautifulSoup


def save_file(url, label, directory):
    file_data = requests.get(url).content
    with open(os.path.join(directory, label), 'wb') as handler:
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
        # I should probably print the actual error
        print(f'{ex}')
        exit()


def figure_out_file_name(soup):
    subject = soup.find('span', {'class': 'subject'}).text
    message = soup.find('blockquote', {'class': 'postMessage'}).text[:15]
    # short circuit - return first letters of the post, if there is no subject
    return subject or message


def file_download_message(idx, all_length, element):
    return f'{idx+1}/{all_length } | {element.text}'


def scrape_files():
    thread_link = sys.argv[1]

    data = fetch_page(thread_link)

    soup = BeautifulSoup(data.text, 'html.parser')

    file_name = figure_out_file_name(soup)

    make_dir(file_name)

    file_elems = (soup.find_all('div', {'class': 'fileText'}))
    for idx, file_elem in enumerate(file_elems):
        anchor = file_elem.find('a')
        # url has a weird formatting
        url = f'http:{anchor.attrs["href"]}'
        label = f'{str(idx).zfill(3)}-{anchor.string}'
        print(file_download_message(idx, len(file_elems), file_elem))
        save_file(url, label, file_name)


def save_to_csv():
    pass


scrape_files()
