"""
New version of the crawler
This creates for every poem from the site a single XML file

Author: Eszter Fodor
Version: 05/2013
"""

import sys
import mechanize
import MySQLdb
import re
import os
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser

import xml.etree.cElementTree as ET
from xml.dom import minidom


"""
Tags to replace in texts
"""
reps = ["<td>", "\t", "\r", "</td>"]


def getPoem(html):
	"""
	Get the poem from the website
	The structure of everywebsite is different which results in the fact that the line
	"find = str(soup.body.table.contents[3].td)" must be changed for every website
	"""
	soup = BeautifulSoup(html)

	find = str(soup.body.table.contents[3].td)
	poemSplit = find.split("<br>")
	poem = strip_tags(poemSplit)
	title = str(soup.body.td.h3.text)
	
	return (poem, title)
	
def strip_tags(text):
	"""
	Strip the text from the tags and replace <br /> with new line
	"""
	for line in text:
		for tag in reps:
			if tag in line:
				line = line.replace(tag, "")
				if "<br />" in line:
					line = line.replace("<br />", "\n")
	return line

def createXML(poem, title):
	root = ET.Element('poem')
	head = ET.SubElement(root, 'phead')
	ptitle = ET.SubElement(head, 'ptitle')
	ptitle.text = title
	author = ET.SubElement(head, 'author')
	first = ET.SubElement(author, 'first-name')
	first.text = 'William'
	second = ET.SubElement(author, 'last-name')
	second.text = 'Shakespeare'
	body = ET.SubElement(root, 'pbody')
	stanza = ET.SubElement(body, 'stanza')
	
	newPoem = poem.split('\n')
	for lines in newPoem:
		if lines == ' ':
			break
		else:
			line = ET.SubElement(stanza, 'line')
			line.text = lines
	root = prettify(root)
	return root
	
def prettify(elem):
    """
    Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
	
def main():
	"""
	Program entry point
	"""
	br = mechanize.Browser()
	site = br.open("http://poetry.eserver.org/sonnets/")
	html = site.read()
	home = BeautifulSoup(html)
	
	links = home.body.tt
	for al in links.findAll('a', href=True):
		newLink = "http://poetry.eserver.org/sonnets/" + str(al['href'])
		ref = br.open(newLink)
		htmlNew = ref.read()
		(poems, title) = getPoem(htmlNew)
		xml = createXML(poems, title)
		
		for i in al:
			fileName = str(i) + '.xml'
			f = open(os.path.join("/media/DATA/AI/EAPoem/Data/Sonnets/", fileName), 'w')
		f.write(xml)

if __name__ == '__main__': main()
