"""
Tool to tag the meter of Shakespearean sonnets
Fairly brute force but necessery
Idea drawn from the paper of E. Greene, T. Bodrumlu and K. Knight:
	Automatic Analysis of Rhythmic Poetry with Applications to Generation and Translation


Author: Eszter Fodor
Version: 06/2013
"""

import os
import re
import sys
import xml.etree.cElementTree as ET
import xml
from xml.dom import minidom
from HTMLParser import HTMLParser
from xml.sax.saxutils import unescape

import nltk
from nltk.corpus import cmudict
from nltk import PorterStemmer 

porter = nltk.PorterStemmer()

meter10 = ['s', 's*', 's', 's*', 's', 's*', 's', 's*', 's', 's*']

d = cmudict.dict()
def nsyl(word):
	"""
	!!! NOT USED !!!
	"""
	print d[word.lower()]
	print [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]] 
 
 
def tagMeter(fileName):
	tree = ET.parse(fileName)
	root = tree.getroot()
	
	for t in root.iter('ptitle'):
		title = t.text
	
	for line in root.iter('line'):
		lineText = ET.SubElement(line, 'text')
		lineText.text = line.text
		line.text = line.text.replace(line.text, "")
		meter = ET.SubElement(line, 'meter')
		meter.text = " ".join([str(x) for x in meter10])
		line = prettify(line)
	
	root = ET.tostring(root, 'utf-8')
	return root, title
	
def prettify(elem):
    """
    Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
		
 

def main(args):
	for fileName in args[1:]:
		with open(fileName) as f:
			(tagged, name) = tagMeter(f)
			fName = (name + "_meterTagged")
			fileName = fName + '.xml'
			nf = open(os.path.join("/media/DATA/AI/EAPoem/Data/SonnetsV2/", fileName), 'w')
			nf.write(tagged)


if __name__ == '__main__':
	sys.exit(main(sys.argv))
	
	
	

	
