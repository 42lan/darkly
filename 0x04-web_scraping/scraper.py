#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

base_url = "http://192.168.56.101/.hidden/"


def writeReadme(text):
  with open("README", "a") as README:
      README.write(text)

def crawl(url):
  result = requests.get(url)
  doc = BeautifulSoup(result.text, "html.parser")
  for current in doc.find_all("a"):
    href = current.get("href")
    if href == "../":
      continue
    elif href == "README":
      file = requests.get(url + href)
      writeReadme(file.text)
    else:
      nextUrl = url + href
      crawl(nextUrl)

crawl(base_url)
