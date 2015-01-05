#!/usr/bin/env python


import os,sys, time, commands
import requests
import urllib2
import xml.etree.ElementTree as ET

class Task(object):
    """Represents a Task template"""
    def __init__(self):
        """Stores xml template for Task
        """   
        self._taskXml = """
    <task>
	<body>%(body)s</body>
	<public type="boolean">%(type)s</public>
	<due-at>%(due-at)s</due-at>
	<subject-id>%(subject-id)s</subject-id>
    </task>"""

       
    def _getTaskTemplate(self):

	return self._taskXml
