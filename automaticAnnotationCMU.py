"""
Automatic annotation

Author: Eszter Fodor
Version 2.0: 06/2013

To run: python automaticAnnotationCMU.py /media/DATA/AI/EAPoem/Data/Sonnets/*.xml
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


rep = ["[", " '", "]", "'", "\n", "(1)", "(2)", "(3)", '"', " ", "(", ")"]
flag = 15

def annotate(fileName):
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
			endDict.update({last.upper():lineNumber})
			counter +=1
		
	annotations = searchRhymes(endDict)

	
	for pair in annotations:
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
	
		
	
def prettify(elem):
    """
    Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    r = rough_string.replace("  ", "")
    reparsed = minidom.parseString(r)
    return reparsed.toprettyxml(indent="  ")
    
    
def searchRhymes(dictionary):
	annotateDictList = []
	for word in dictionary.keys():
		d = {}
		wordLine = dictionary[word]
		arg = ("['"  + word + "', ") # "['WET', "
		try:
			rhymes = subprocess.check_output(["fgrep","-m 1", arg, "/media/DATA/AI/Scriptie/Dictionaries/cmuFour.txt"], stderr=subprocess.STDOUT)
			rhymesList = rhymes.split(",")
			
			for i in range(len(rhymesList)):
				for tag in rep:
					if tag in rhymesList[i]:
						rhymesList[i] = rhymesList[i].replace(tag, "")
			
			primary = rhymesList[0]
			del dictionary[word]
			
			for other in dictionary.keys():
				if other in rhymesList or other == word:
					d[word] = wordLine
					d[other] = dictionary[other]
					annotateDictList.append(d)
										
			
		except KeyboardInterrupt:
			sys.exit(0)
		except:
			print 'Word not found in dictionary: ' + word + '. Skipping word...'
			pass
	
	return annotateDictList		

def main(args):
	begin = time.time()
	for fileName in args[1:]:
		with open(fileName) as f:
			(xml,t) = annotate(f)
			#(xml, name) = newXML(l, r)
			fName = (t.replace(" ", "")+ 'ann')
			fileName = fName.lower() + '.xml'
			nf = open(os.path.join("/media/DATA/AI/EAPoem/Data/AccuracyCheck/ann2", fileName), 'w')
			nf.write(xml)
			
			
	end = time.time()-begin
	print 'Time taken: %d min and %d sec' % (end/60, end%60)
			
	

if __name__ == '__main__':
	sys.exit(main(sys.argv))
