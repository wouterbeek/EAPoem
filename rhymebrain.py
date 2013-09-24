"""
Rhymebrain crawler and annotater

Adapted version of automaticAnnotationCMU.py

Author: Eszter Fodor
Version 1.0: 06/2013
"""

import signal
import sys
import os
import re
import subprocess
import xml.etree.cElementTree as ET
from xml.dom import minidom
import time
import xml
from xml.sax.saxutils import unescape

from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser as p
import mechanize

flag = 15

def getRhymes(searchWord):
	"""
	Constructs list with all the words that came up on the site
	"""
	br = mechanize.Browser()
	link = ('http://rhymebrain.com/en/What_rhymes_with_%s.html' % searchWord)
	site = br.open(link)
	html = site.read()
	soup = BeautifulSoup(html)
	find = soup.body.findAll('span')
	rhymeWords = [span.text for span in find]
	site.close()
	
	return rhymeWords
	
	
def annotate(fileName):
	annotateDictList = []
	endDict = dict([])
	tree = ET.parse(fileName)
	root = tree.getroot()
	counter = 1
	
	for t in root.iter('ptitle'):
		title = t.text
		
	for line in root.iter('line'):
		if (counter != flag):
			lineSplit = line.text.split(" ")
			lineSplitReversed = lineSplit[::-1]
			last = lineSplitReversed[0]
			lineNumber = counter
			endDict.update({last:lineNumber})
			counter +=1
			
	for firstWord, valOne in endDict.items():
		d = {}
		try:
			lineNumber = valOne
			possibilities = getRhymes(firstWord)
			del endDict[firstWord]
		
			for otherWords, valTwo in endDict.items():
				
				if otherWords in possibilities:
					secondLineNumber = valTwo
					del endDict[otherWords]
					
					d[firstWord] = lineNumber
					d[otherWords] = secondLineNumber
					
		except KeyboardInterrupt:
			sys.exit(0)			
		except:
			pass
		
		if d:
			annotateDictList.append(d)
			
	for pair in annotateDictList:
		for key, val in pair.items():
			if val == 1 or val == 3:
				a = ET.SubElement(root[1][0][val-1], 'phoneme', category = 'a')
				a.text = key.lower()
				root[1][0][val-1].text = root[1][0][val-1].text.rsplit(' ', 1)[0]
			elif val == 2 or val == 4:
				b = ET.SubElement(root[1][0][val-1], 'phoneme', category = 'b')
				b.text = key.lower()
				root[1][0][val-1].text = root[1][0][val-1].text.rsplit(' ', 1)[0]
			elif val == 5 or val == 7:
				c = ET.SubElement(root[1][0][val-1], 'phoneme', category = 'c')
				c.text = key.lower()
				root[1][0][val-1].text = root[1][0][val-1].text.rsplit(' ', 1)[0]
			elif val == 6 or val == 8:
				d = ET.SubElement(root[1][0][val-1], 'phoneme', category = 'd')
				d.text = key.lower()
				root[1][0][val-1].text = root[1][0][val-1].text.rsplit(' ', 1)[0]
			elif val == 9 or val == 11:
				e = ET.SubElement(root[1][0][val-1], 'phoneme', category = 'e')
				e.text = key.lower()
				root[1][0][val-1].text = root[1][0][val-1].text.rsplit(' ', 1)[0]
			elif val == 10 or val == 12:
				f = ET.SubElement(root[1][0][val-1], 'phoneme', category = 'f')
				f.text = key.lower()
				root[1][0][val-1].text = root[1][0][val-1].text.rsplit(' ', 1)[0]
			elif val == 13 or val == 14:
				g = ET.SubElement(root[1][0][val-1], 'phoneme', category = 'g')
				g.text = key.lower()
				root[1][0][val-1].text = root[1][0][val-1].text.rsplit(' ', 1)[0]
				
	return xml.sax.saxutils.unescape(ET.tostring(root, 'utf-8')), title
			
		
def main(args):
	begin = time.time()
	for fileName in args[1:]:
		with open(fileName) as f:
			(xml, t) = annotate(f)
			#(xml, name) = newXML(l, r)
			fName = (t.replace(" ", "")+ 'ann')
			fileName = fName.lower() + '.xml'
			nf = open(os.path.join("/media/DATA/AI/EAPoem/Data/RhymeBrainTest/ann", fileName), 'w')
			nf.write(xml)
			
			
			
	end = time.time()-begin
	print 'Time taken: %d min and %d sec' % (end/60, end%60)
			
	

if __name__ == '__main__':
	sys.exit(main(sys.argv))

