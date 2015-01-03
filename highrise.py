#!/usr/bin/env python


import os,sys, time, commands
import requests
import urllib2

import xml.etree.ElementTree as ET

def printMainMenu():
  print "1. List Contacts"
  print "2. Create Contact"
  print "3. List Task/s"
  print "4. Create Task"
  print "5. Search User"
  print "6. Exit"
  try:
    choice = input("\n\nPlease Select Operation[1-6]:")
  except SyntaxError:
    choice = -1
  except NameError:
    choice = -1
  except:
    sys.stderr.write("Unknown Error in User Interface\n")
    sys.exit(1)
  return choice




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
       
    def connection(self):
	password = 'X'
	passmanager = urllib2.HTTPPasswordMgrWithDefaultRealm()
	passmanager.add_password(None, self._url, self._privateToken, password)
	authhandler = urllib2.HTTPBasicAuthHandler(passmanager)
	self.opener = urllib2.build_opener(authhandler)


    def listContacts(self):
	contactList = []
	urllib2.install_opener(self.opener)
	page = urllib2.urlopen("%s/people.xml" % self._url).read()
	root = ET.fromstring(page)

	for person in root.findall('person'):
		name = "%s %s" % ( person.find('first-name').text, person.find('last-name').text)
		contactList.append(name)

	self.printTable(contactList)
	
        return 


    
    def createContact(self):
	return



    def createTask(self):
	return


    def listTasks(self):
	return


    def searchContact(self):
	return

    def printTable(self,elements,spacing=45):
        if self._printFlag:
		for each in elements:
                	print '|'.join(['%s' % each.center(spacing)])
                        print "\n"
        return



def main(argv=sys.argv):
  os.system('clear')
  print "Welcome to the HighRise User Management tool"
  print "What would you like to do today?\n\n\n"

  while(1):
    choice = printMainMenu()
    while (choice < 1 or choice > 6):
      os.system('clear')
      print "-----Invalid Selection-----"
      print "Please Choose one of the following:"
      choice = printMainMenu()
    if choice == 6:
      print "Goodbye"
      sys.exit(1)
    else:	
     hl = Highrise("https://organization223.highrisehq.com","77427d6a0fae05a6bd5a34df27221ab1")
     hl.connection()

     #mainOp[] is a list  of function pointers, it just allows us to write things a bit more cleanly for a menu driven interface
     mainOp = [hl.listContacts,hl.createContact,hl.listTasks,hl.createTask,hl.searchContact]

     mainOp[choice - 1]()  #yes, this is a function call


if __name__ == "__main__":
  main()  
