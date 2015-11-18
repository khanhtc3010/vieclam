from pymongo import *
import os.path
from os.path import isfile,join
import env_config 

"""For config and db classes"""
class Singleton(object):
	instance = None
	
	def __setattr__(self, attr, value):
		return setattr(self.instance, attr, value) #self.instance.attr = value

	def __getattr__(self, attr):
		return getattr(self.instance, attr) # = None if not has attr || = value if has attr

	def setAttributes(self, attributeDict):
		for attribute, attributeValue in attributeDict.iteritems():
			setattr(self, attribute, attributeValue)


class Config(Singleton):
	instance = None

	def __init__(self):
		if Config.instance is None:
			Config.instance = Config.__Singleton()

	class __Singleton:
		def __init__(self):
			config = env_config.config()
			self.dbhost = config["mongo"]["host"]
			self.dbname = config["mongo"]["dbname"]
			self.username = config["mongo"]["username"]
			self.password = config["mongo"]["password"]
			self.dbport = config["mongo"]["port"]
			self.env = config["environment"]



class DBConnection(Singleton):
	instance = None

	def __init__(self):
		if DBConnection.instance is None:
			DBConnection.instance = DBConnection.__Singleton()

	class __Singleton:
		def __init__(self):
			settings = Config()
			self.connection = MongoClient(
			    settings.dbhost,
			    settings.dbport
			)
			self.db = self.connection[settings.dbname]

		
"""End***************"""