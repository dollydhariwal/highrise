#!/usr/bin/env python


import os,sys, time, commands
import requests
import urllib2
import xml.etree.ElementTree as ET

class Note(object):
    """Represents a Task template"""
    def __init__(self):
        """Stores xml template for Task
        """   
        self._noteXml = """
    <note>
	<body>%(body)s</body>
	<subject-id type="integer">%(subject)s</subject-id>
	<subject-type>%(type)s</subject-type>
    </note>"""

       
    def _getNoteTemplate(self):

	return self._noteXml
