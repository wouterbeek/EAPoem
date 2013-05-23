"""
New version of the crawler
This creates for every poem from the site a single XML file

Author: Eszter Fodor
"""

import sys
import mechanize
import MySQLdb
import re
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser

import xml.etree.cElementTree as ET

def createXML(poem, title):
	root = Element('poem')
	child = SubElement(root, 'phead')
	child2 = SubElement(child, 'ptitle')
	child2.text = "%s", title
