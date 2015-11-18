from sysclass import *
import requests, urllib2
from bs4 import BeautifulSoup
from pymongo import *
import mojigoi, kanji, bunbou, dokkai, choukai

class Somatome(object):
	def __init__(self):
		self.data = None
		self.url = None
		self.level = None
		self.html = None
		self.code = None
		connection = DBConnection()
		self.db = connection.db

	def setUrl(self, url):
		self.url = url

	def requestHTML(self):
		#response = requests.get(self.url)
		if self.url.find('http://') < 0:
			self.url = "http://"+self.url
		response = urllib2.urlopen(urllib2.Request(self.url))
		self.html = response

	def extractHTML(self):
		pass

	def saveToDB(self):
		self.collection.insert_one(self.data)

	def run(self):
		self.requestHTML()
		self.extractHTML()
		self.saveToDB()


class Mojigoi(Somatome):
	def __init__(self):
		Somatome.__init__(self)
		self.collection = self.db.mojigoi


	def extractHTML(self):
		soup = BeautifulSoup(self.html, 'html.parser')
		# TODO: extract html here
		data = mojigoi.htmlToData(soup)
		self.data = data
		


class Kanji(Somatome):
	def __init__(self):
		Somatome.__init__(self)
		self.collection = self.db.kanji

	def extractHTML(self):
		soup = BeautifulSoup(self.html, 'html.parser')
		# TODO: extract html here
		data = kanji.htmlToData(soup)
		self.data = data

class Bunbou(Somatome):
	def __init__(self):
		Somatome.__init__(self)
		self.collection = self.db.bunbou

	def extractHTML(self):
		soup = BeautifulSoup(self.html, 'html.parser')
		data = bunbou.htmlToData(soup)
		self.data = data

class Dokkai(Somatome):
	def __init__(self):
		Somatome.__init__(self)
		self.collection = self.db.dokkai

	def extractHTML(self):
		soup = BeautifulSoup(self.html, 'html.parser')
		data = dokkai.htmlToData(soup)
		self.data = data

class Choukai(Somatome):
	def __init__(self):
		Somatome.__init__(self)
		self.collection = self.db.choukai

	def extractHTML(self):
		soup = BeautifulSoup(self.html, 'html.parser')
		data = choukai.htmlToData(soup)
		self.data = data