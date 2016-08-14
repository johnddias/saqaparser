#!/usr/bin/env python

import logging
import sys
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup, SoupStrainer
import requests
import inquirer

only_transcripts = SoupStrainer(sasource="qp_transcripts")

def gettranscripts ( ticker ):
    "Gets a list of available transcripts for a valid stock ticker"
    turl = "http://seekingalpha.com/symbol/%s/transcripts" % (ticker)
    tres = requests.get(turl, headers=headers)
    tsoup = BeautifulSoup(tres.text, 'html.parser', parse_only=only_transcripts)
    picklist = []
    for t in tsoup:
        picklist.append(t.string)
    return picklist;

def gethref ( ticker,article ):
    "Finds the href for the selected article title string"
    turl = "http://seekingalpha.com/symbol/%s/transcripts" % (ticker)
    tres = requests.get(turl, headers=headers)
    tsoup = BeautifulSoup(tres.text, 'html.parser', parse_only=only_transcripts)
    href = ""
    for t in tsoup:
        if t.string == article:
            href=t['href']
            return href;

headers = {
    'User-Agent': 'Mozzila/5.0'
}

tick = raw_input('Ticker Symbol: ')
picklist = gettranscripts(tick)
questions = [
    inquirer.List('article',
            message = 'Select an article to process...',
            choices = picklist,
    ),
]
article = inquirer.prompt(questions)

targeturl = gethref(tick,article['article'])
url = "http://seekingalpha.com" + targeturl + "?part=single"
response = requests.get(url, headers=headers)
#print(response.status_code)
#print(response.headers)
soup = BeautifulSoup(response.text, 'html.parser')

transcript = soup.find(id="a-body")
fo = open("qanda.txt", "w")
for i in transcript.children:
    t = i.string
    if t:
        fo.write(t.encode('utf-8'))
        fo.write("\n")
fo.close()
