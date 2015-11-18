#!/usr/bin/python
#-*- coding:utf-8 -*-
from myLib import *
import requests
import Queue, thread, time

link = "http://vieclam.tv/timungvien/"
response = requests.get(link, params = {"page":"2"})
soup = readSoup(response.url)
codecs.open("vieclam.html", "w", "utf-8").write(soup.prettify())