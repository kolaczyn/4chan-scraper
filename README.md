# Scrape Chan

This is a 4chan scraper written in Python. You should be able to download anything from any board - images and videos

## Setup and Usage Example

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
pipenv shell

# to scrape, 
python scrape_chan.py https://boards.4channel.org/g/thread/76759434

```

You don't have to wrap the links in **'parenthesis'**, because the links to 4chan threads don't seem to include special characters like **&**.


## User Stories

- You can download all the files in a given thread
- You can download thumbnails
- Progress bar
- Show what you're downloading, the size, you can cancel downloading that file
- You can say that you only want jpg, png, wemb or gif
- Limit how many you want
- You can come back leter and download ony new file and you don't have to redownload the old ones