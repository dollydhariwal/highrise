#!/usr/bin/env python


import os,sys, time, commands
import requests
import urllib2
import xml.etree.ElementTree as ET

class People(object):
    """Represents a People template"""
    def __init__(self):
        """Stores xml template for people
        """   
        self._peopleXml = """
    <person>
        <first-name>%(first-name)s</first-name>
        <last-name>%(last-name)s</last-name>
        <title>%(title)s</title>
     </person>"""

       
    def _getPeopleTemplate(self):

	return self._peopleXml
