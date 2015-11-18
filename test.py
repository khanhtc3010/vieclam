#!/usr/bin/python
#-*- coding:utf-8 -*-
from myLib import *
import requests
import Queue, thread, time
from pymongo import *

client = MongoClient('localhost', 27017)
db = client.vieclam
ungvien = db.ungvien

link = "http://vieclam.tv/ungvien/uv-pham-dang-dien-phamdangdien-53ckct-gmail-com-01674903404/bp1n"
#link = "http://vieclam.tv/ungvien/uv-ngo-tran-duy-duyngo-interior-gmail-com-0934813093/b1cy"
# response = requests.get(link, params = {"page":"2"})
# soup = readSoup(response.url)
# box_uv = soup.find('div', attrs = {'id':'box-ungvien'})
# tr_list = box_uv.find_all('tr')
# for j in xrange(1, len(tr_list)):
# 	link = "http://vieclam.tv"+tr_list[j].td.a['href']
# 	print link
# cv
# qualifications
# experiences
# works
# contact
soup = readSoup(link)
title = soup.title.text.strip()
flag = title.find("mã số: ".decode("utf-8"))
data = {}
data["cv"] = {}
data["qualifications"] = {}
data["experiences"] = {}
data["works"] = {}
data["contact"] = {}
data["id"] = title[flag+7:]
######################################################
info_list = soup.find('div', {'class':'dk-info'}).find_all('tr')
data["cv"]["name"] = info_list[0].find_all('td')[1].text.strip()
data["cv"]["birth"] = info_list[1].find_all('td')[1].text.strip()
data["cv"]["gender"] = info_list[2].find_all('td')[1].text.strip()
try:
	data["cv"]["img"] = "img/"+data["id"]+".jpg"
	img_link = "http://vieclam.tv"+info_list[3].img['src']
	urllib.urlretrieve(img_link, data["cv"]["img"])
except:
	pass
######################################################
ungvien.insert_one(data)