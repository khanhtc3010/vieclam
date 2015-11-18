# -*- coding: utf-8 -*-
import urllib2, urllib, requests
import codecs, datetime
from bs4 import BeautifulSoup

#tra ve html dang soup san sang cho viec crawl
def readSoup(url):
    if url.find('http://') < 0:
        url = "http://" + url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, 'html.parser')
    return soup

def saveLog(url, note):
	f = codecs.open("log.txt", "a", "utf-8")
	time = datetime.datetime.now()
	f.write(time+"\t"+unicode(url)+"\n"+unicode(note)+"\n")
	f.close