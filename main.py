#!/usr/bin/python
#-*- coding:utf-8 -*-
from topclass import *
from myLib import *
import Queue, thread, time

q = Queue.Queue(maxsize=0)

def mainPage():
	f1 = codecs.open("link.txt", 'a', 'utf-8')
	origLink = "http://vieclam.tv/timungvien/?page="
	for i in xrange(1, 6407):
		soup = readSoup(origLink+str(i))
		box_uv = soup.find('div', attrs = {'id':'box-ungvien'})
		tr_list = box_uv.find_all('tr')
		for j in xrange(1, len(tr_list)):
			link = "http://vieclam.tv"+tr_list[j].td.a['href']
			f1.write(link+"\n")
			q.put(link)
			crawlData(link)
	f1.close

def crawlData(link):
	print "crawling page: "+link
	try:
		uv = Ungvien()
		uv.setUrl(link)
		uv.run()
	except Exception as error:
		saveLog(link, error)

if __name__ == '__main__':
	mainPage()
	while not q.empty():
		thread.start_new_thread(crawlData, (q.get(),))
		print "Start a new crawler thread..."
		time.sleep(2)