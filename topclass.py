#!/usr/bin/python
#-*- coding:utf-8 -*-
from sysclass import *
import requests, urllib2
from bs4 import BeautifulSoup
from pymongo import *
from myLib import *

class Ungvien(object):
	def __init__(self):
		self.data = {}
		self.url = None
		self.html = None
		connection = DBConnection()
		self.db = connection.db
		self.collection = self.db.ungvien

	def setUrl(self, url):
		self.url = url

	def getHTML(self):
		self.html = readSoup(self.url)

	def extractHTML(self):
		#crawl data here, data store in self.data
		self.data = htmlToData(self.html)

	def saveToDB(self):
		self.collection.insert_one(self.data)

	def run(self):
		self.getHTML()
		self.extractHTML()
		self.saveToDB()

#FUNCTIONS
def htmlToData(soup):
	title = soup.title.text.strip()
	flag = title.find("mã số: ".decode("utf-8"))
	data = {}
	data["cv"] = {}
	data["qualifications"] = {}
	data["experiences"] = {}
	data["job"] = {}
	data["contact"] = {}
	data["id"] = title[flag+7:]
	######################################################
	data["cv"] = cvData(soup.find('div', {'class':'dk-info'}).find_all('tr'), data["id"])
	table = soup.find_all('div', {'class':'viecchitiet'})
	data["qualifications"] = qualificationsData(table[0])
	data["experiences"] = experiencesData(table[1])
	data["job"] = jobData(table[2])
	data["contact"] = contactData(table[3])
	######################################################
	return data

def cvData(info_list, _id):
	cv = {}
	cv["name"] = info_list[0].find_all('td')[1].text.strip()
	cv["birth"] = info_list[1].find_all('td')[1].text.strip()
	cv["gender"] = info_list[2].find_all('td')[1].text.strip()
	try:
		cv["img"] = "img/"+_id+".jpg"
		img_link = "http://vieclam.tv"+info_list[3].img['src']
		urllib.urlretrieve(img_link, cv["img"])
	except:
		pass
	return cv

def qualificationsData(table):
	qualifications = {}
	tr_list = table.find_all('tr')
	try:
		qualifications["level"] = tr_list[0].find_all('td')[1].text.strip()
		qualifications["graduate"] = int(tr_list[0].find_all('td')[3].text.strip())
	except:
		qualifications["graduate"] = None
	qualifications["course"] = tr_list[1].find_all('td')[1].text.strip()
	qualifications["class"] = tr_list[1].find_all('td')[3].text.strip()
	qualifications["university"] = tr_list[2].find_all('td')[1].text.strip()
	qualifications["language"] = tr_list[3].find_all('td')[1].text.strip().split(','.decode('utf-8'))
	qualifications["it"] = tr_list[4].find_all('td')[1].text.strip()
	qualifications["license"] = tr_list[5].find_all('td')[1].text.strip().split(','.decode('utf-8'))
	return qualifications

def experiencesData(table):
	experiences = {}
	tr_list = table.find_all('tr')
	try:
		experiences["time"] = int(tr_list[0].find_all('td')[1].text.strip()\
							.replace('năm'.decode('utf-8'), '')\
							.replace('Trên '.decode('utf-8'), '+')\
							.replace('Dưới '.decode('utf-8'), '-')\
							.replace('Chưa có KN'.decode('utf-8'), '0'))
	except:
		experiences["time"] = None
	experiences["exper"] = tr_list[1].find_all('td')[1].text.strip()
	experiences["skill"] = tr_list[2].find_all('td')[1].text.strip()
	return experiences

def jobData(table):
	job = {}
	tr_list = table.find_all('tr')
	job["work"] = tr_list[0].find_all('td')[1].text.strip().split(','.decode('utf-8'))
	job["rank"] = tr_list[1].find_all('td')[1].text.strip()
	job["trades"] = tr_list[2].find_all('td')[1].text.strip()
	job["type"] = tr_list[3].find_all('td')[1].text.strip()
	job["location"] = tr_list[4].find_all('td')[1].text.strip().split(','.decode('utf-8'))
	try:
		data["salary"] = {}
		salary = tr_list[5].find_all('td')[1].text.strip().replace('triệu'.decode('utf-8'), '')
		if '-'.decode('utf-8') in salary:
			salary = salary.split('-'.decode('utf-8'))
			data["salary"]["min"] = int(salary[0].strip())
			data["salary"]["max"] = int(salary[1].strip())
		else:
			data["salary"]["min"] = int(salary.replace('Trên'.decode('utf-8'), '')).strip()
	except:
		job["salary"] = 0
	job["target"] = tr_list[6].find_all('td')[1].text.strip()
	return job

def contactData(table):
	contact = {}
	tr_list = table.find_all('tr')
	contact["name"] = tr_list[0].find_all('td')[1].text.strip()
	contact["email"] = tr_list[1].find_all('td')[1].text.strip()
	contact["phone_number"] = tr_list[2].find_all('td')[1].text.strip()
	return contact