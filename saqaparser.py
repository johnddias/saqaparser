#!/usr/bin/env python

import logging
import sys
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozzila/5.0'
}

url = "http://seekingalpha.com/article/3989264-vmwares-vmw-ceo-patrick-gelsinger-q2-2016-results-earnings-call-transcript"
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.headers)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())
