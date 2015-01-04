#!/usr/bin/env python


import os,sys, time, commands
import requests
import urllib2
import xml.etree.ElementTree as ET
sys.path.insert(1, '%s/templates' % os.getcwd())
from people import *

class Highrise(object):
    """Represents a Highrise server connection"""
    def __init__(self,url,privateToken=None):
        """Stores information about the server   
        url : the URL of the highrise server
        private_token: the user private token
        email: the user email/login
        password: the user password (associated with email)
        """   
        self._url = '%s' % url
        self._privateToken = privateToken
	self._printFlag = True
	self._connection()
	self._contactDict = self._createContactDict()
	self._taskDict = self._createTaskDict()

       
    def _connection(self):
	password = 'X'
	passmanager = urllib2.HTTPPasswordMgrWithDefaultRealm()
	passmanager.add_password(None, self._url, self._privateToken, password)
	authhandler = urllib2.HTTPBasicAuthHandler(passmanager)
	self.opener = urllib2.build_opener(authhandler)



    def _createContactDict(self):
        urllib2.install_opener(self.opener)
        page = urllib2.urlopen("%s/people.xml" % self._url).read()
        root = ET.fromstring(page)

	contactDict = {}
        for person in root.findall('person'):
                name = "%s %s" % ( person.find('first-name').text, person.find('last-name').text)
                contactDict[person.find('id').text] = name

        return contactDict	


    def _createTaskDict(self):
        urllib2.install_opener(self.opener)
        page = urllib2.urlopen("%s/tasks.xml" % self._url).read()
        root = ET.fromstring(page)

        taskDict = {}
        for task in root.findall('task'):
                taskDict[task.find('body').text] = task.find('author-id').text

        return taskDict


    def listContacts(self):
	contactList = []
	urllib2.install_opener(self.opener)
	page = urllib2.urlopen("%s/people.xml" % self._url).read()
	root = ET.fromstring(page)

	for person in root.findall('person'):
		name = "%s %s" % ( person.find('first-name').text, person.find('last-name').text)
		contactList.append(name)
		self._contactDict[name] = person.find('author-id').text

	self.printTable(contactList)
	print self._contactDict
	
        return 


    
    def createContact(self):
        os.system('clear')
        print "This task is to create a contact"
        print "Give the contact details to be created\n\n\n"

        firstName = raw_input("Please Enter the First Name of the contact to be created: ")
        lastName = raw_input("Please Enter the Last Name of the contact to be created: ")
        title = raw_input("Please Enter the Title of the contact to be created: ")

	xmlTemplate = People()._getPeopleTemplate()
	data = {'first-name': firstName, 'last-name': lastName, 'title': title}
	xml_string =  xmlTemplate%data
	url = "%s/people.xml" % self._url

	try:
	        urllib2.install_opener(self.opener)
		req = urllib2.Request(url=url, 
                	      data=xml_string, 
	                      headers={'Content-Type': 'application/xml'})
		urllib2.urlopen(req)

		print "The user %s %s has been created successfully " % (firstName, lastName)
	except:
		print "The tool was not able to add user %s %s " % (firstName, lastName)
	
	return


    def createAutoTask(self, id):
	body = "Task for user %s" % (self._contactList[id])
        dueAt = raw_input("Please Enter the Due At date for the task : ")
        title = raw_input("Please Enter the Title of the contact to  ")
	



    def createTask(self):
	return


    def listTasks(self):
        taskList = []
        urllib2.install_opener(self.opener)
        page = urllib2.urlopen("%s/tasks.xml" % self._url).read()
        root = ET.fromstring(page)

        for task in root.findall('task'):
		if task.find('subject-id').text is not None :
	                taskString = "%s | %s | %s | %s" % ( task.find('body').text, task.find('created-at').text,  self._contactDict[task.find('subject-id').text], task.find('due-at').text)
		else:
	                taskString = "%s | %s | %s" % ( task.find('body').text, task.find('created-at').text, task.find('due-at').text)

       	        taskList.append(taskString)

        self.printTable(taskList)
	return


    def searchContact(self):
	return

    def printTable(self,elements,spacing=45):
        if self._printFlag:
		for each in elements:
                	print '|'.join(['%s' % each.center(spacing)])
                        print "\n"
        return
