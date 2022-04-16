#!/bin/bash

#Can 'EmreYbs' find a job at https://jobs.kent.ac.uk :)?
#On purpose, I didn't use Pandas and save as csv, since this small code is only for my job hunt for a specific site.There won't be many Announcements there:)
#So no need to use data frames.

import requests
from bs4 import BeautifulSoup

from halo import Halo
import time


print("\n\tJob Announcements at the University of Kent Website")
print("\n\tThis simple Python code will download the RSS Feeds for Job Announcements in the University of Kent Website\n")

spinner = Halo(text="I will download the RSS Feed for Jobs now...\n",spinner="dots",color="cyan", text_color="red")
spinner.start()
time.sleep(4)
spinner.stop()

url = requests.get('https://jobs.kent.ac.uk/RSS/rss.aspx?cat=205&type=9')
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'}

soup = BeautifulSoup(url.content, 'xml')
items = soup.find_all('item')


for item in items:
    title = item.title.text
    
    link = item.link.text
    category = item.category.text
    pubDate = item.pubDate.text
    print(f"\tTitle: {title}\n\n\tLink: {link}\n\nCategory: {category}\n\npubDate: {pubDate}")

print("\nHope, you can find a suitable job for yourself mate...\n")
spinner = Halo(text="Finished scraping latest job announcements.\n",spinner="dots",color="cyan", text_color="magenta")
spinner.start()
time.sleep(2)
spinner.stop()
