# Scrape Chan

This is a 4chan scraper written in Python. You should be able to download anything from any board - images and videos.

## Setup

You need to have the following pieces of software installed on your system:

- git
- Python 3, at least 3.6
- pip
- [pipenv](https://pipenv.pypa.io/en/latest/)

Run the following commands:

```
git clone https://github.com/kolaczyn/4chan-scraper.git
cd 4chan-scraper

pipenv install
```

## How to use it

It looks self explanatory - the first argument of the application is the link to the thread you want to scrape.

```
# enter the virtual environment
pipenv shell

python scrape_chan.py https://boards.4channel.org/g/thread/76759434
python scrape_chan.py https://boards.4channel.org/sci/thread/5942502

```

After it finishes downloading, you can find the scraped files in the `threads/` folder.

You don't have to wrap the links in `''` or `""` because the links to 4chan threads don't seem to include special characters like `&`.

## User Stories

List of features I want to add in the future.

- You can download thumbnails
- Show what you're downloading, the size, you can cancel downloading that file
- You can say that you only want jpg, png, wemb or gif
- Limit how many you want
- You can come back leter and download ony new file and you don't have to redownload the old ones
