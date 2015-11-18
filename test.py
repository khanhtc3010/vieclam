#!/usr/bin/python
#-*- coding:utf-8 -*-
from myLib import *
import Queue, thread, time, mechanize


br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

link = "http://vieclam.tv/timungvien/"

soup = BeautifulSoup(br.open(link), 'lxml')
codecs.open("vieclam.html", "w", "utf-8").write(soup.prettify())

response = br.follow_link(text='Tiếp')
soup = BeautifulSoup(response, 'lxml')
codecs.open("next.html", "w", "utf-8").write(soup.prettify())