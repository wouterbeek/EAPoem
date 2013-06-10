"""
Brute force rhyme annotation
Neccesery measures to be able to progress to next stage

This version creates better xmls

Author: Eszter Fodor
Version 3.0, 06/2013
"""

import os
import re
import sys
import xml.etree.cElementTree as ET
import xml
from xml.dom import minidom
from HTMLParser import HTMLParser
from xml.sax.saxutils import unescape


def annotate(fileName):
	newLines = []
	tree = ET.parse(fileName)
	root = tree.getroot()
	counter = 1
	
	for t in root.iter('ptitle'):
		title = t.text
	
	for line in root.iter('line'):
		lineSplit = line.text.split(" ")
		lineSplitReversed = lineSplit[::-1]
		last = lineSplitReversed[0]
		lineNumber = counter
		if lineNumber == 1 or lineNumber == 3:
			a = ET.SubElement(line, 'phoneme', category = 'a')
			a.text = last
		elif lineNumber == 2 or lineNumber == 4:
			b = ET.SubElement(line, 'phoneme', category = 'b')
			b.text = last
		elif lineNumber == 5 or lineNumber == 7:
			c = ET.SubElement(line, 'phoneme', category = 'c')
			c.text = last
		elif lineNumber == 6 or lineNumber == 8:
			d = ET.SubElement(line, 'phoneme', category = 'd')
			d.text = last
		elif lineNumber == 9 or lineNumber == 11:
			e = ET.SubElement(line, 'phoneme', category = 'e')
			e.text = last
		elif lineNumber == 10 or lineNumber == 12:
			f = ET.SubElement(line, 'phoneme', category = 'f')
			f.text = last
		elif lineNumber == 13 or lineNumber == 14:
			g = ET.SubElement(line, 'phoneme', category = 'g')
			g.text = last
		lineSplitReversed[0] = last
		newLine = lineSplitReversed[::-1]
		newLines.append(newLine)
		counter +=1
	return xml.sax.saxutils.unescape(ET.tostring(root, 'utf-8')), title
	
		
	
def prettify(elem):
    """
    Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    r = rough_string.replace("  ", "")
    reparsed = minidom.parseString(r)
    return reparsed.toprettyxml(indent="  ")
		

def main(args):
	for fileName in args[1:]:
		with open(fileName) as f:
			(xml,t) = annotate(f)
			#(xml, name) = newXML(l, r)
			fName = (t + "_ann")
			fileName = fName + '.xml'
			nf = open(os.path.join("/media/DATA/AI/EAPoem/Data/SonnetsV3", fileName), 'w')
			nf.write(xml)
	

if __name__ == '__main__':
	sys.exit(main(sys.argv))
