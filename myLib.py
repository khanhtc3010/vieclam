# -*- coding: utf-8 -*-
import urllib2, urllib, codecs
from bs4 import BeautifulSoup
#ham loai bo cac ki tu dinh dang in khoi string
def handleString(string):
	flag = 0
	try:
		for i in xrange(len(string)):
			if string[i] in ['\n','\t','\r']:
				i += 1
				flag = i
		string = string[flag:]
	except:
		string = " "
	return string

#tra ve html dang soup san sang cho viec crawl
def readSoup(url):
    if url.find('http://') < 0:
        url = "http://" + url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, 'lxml')
    return soup