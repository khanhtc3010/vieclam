from topclass import *
from myLib import *
import Queue, thread, time, mechanize

q = Queue.Queue(maxsize=0)
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def getLink(url):
	soup = readSoup(url)
	for url in soup.find_all('td', attrs = {'class':'list-title'}):
		link = "www.vnjpclub.com"+url.a['href']
		q.put(link)

def mainPage():
	origLink = "http://vieclam.tv/timungvien/"
	soup = readSoup(origLink)
	for url in soup.find_all('a'):
		try:
			url = url['href']
			if url.find('soumatome-n3') >= 0:
				link = "www.vnjpclub.com" + url
				getLink(link)
		except:
			return

def crawlData(link):
	

if __name__ == '__main__':
	mainPage()
	while not q.empty():
		thread.start_new_thread(crawlData, (q.get(),))
		print "Start a new crawler thread..."
		time.sleep(2)