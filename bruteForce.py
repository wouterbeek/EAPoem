"""
Brute force rhyme annotation
Neccesery measures to be able to progress to next stage
"""

import os
import re
import sys
import xml.etree.cElementTree as ET
from xml.dom import minidom
from HTMLParser import HTMLParser
from xml.sax.saxutils import unescape


def annotate(fileName):
	newLines = []
	tree = ET.parse(fileName)
	root = tree.getroot()
	counter = 1
	for line in root.iter('line'):
		lineSplit = line.text.split(" ")
		lineSplitReversed = lineSplit[::-1]
		last = lineSplitReversed[0]
		lineNumber = counter
		if lineNumber == 1 or lineNumber == 3:
			last = ("(a)" + last + "(/a)")
		elif lineNumber == 2 or lineNumber == 4:
			last = ("(b)" + last + "(/b)")
		elif lineNumber == 5 or lineNumber == 7:
			last = ("(c)" + last + "(/c)")
		elif lineNumber == 6 or lineNumber == 8:
			last = ("(d)" + last + "(/d)")
		elif lineNumber == 9 or lineNumber == 11:
			last = ("(e)" + last + "(/e)")
		elif lineNumber == 10 or lineNumber == 12:
			last = ("(f)" + last + "(/f)")
		elif lineNumber == 13 or lineNumber == 14:
			last = ("(g)" + last + "(/g)")
		lineSplitReversed[0] = last
		newLine = lineSplitReversed[::-1]
		newLines.append(newLine)
		counter +=1
	return newLines, root
		
def newXML(lines, oldRoot):
	
	for t in oldRoot.iter('ptitle'):
		title = t.text
		
	
	root = ET.Element('poem')
	head = ET.SubElement(root, 'phead')
	ptitle = ET.SubElement(head, 'ptitle')
	ptitle.text = (title + " annotated")
	author = ET.SubElement(head, 'author')
	first = ET.SubElement(author, 'first-name')
	first.text = 'William'
	second = ET.SubElement(author, 'last-name')
	second.text = 'Shakespeare'
	body = ET.SubElement(root, 'pbody')
	stanza = ET.SubElement(body, 'stanza')
	
	for li in lines:
		w = " ".join([str(x) for x in li])
		line = ET.SubElement(stanza, 'line')
		line.text = w
	root = prettify(root)
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
			(l,r) = annotate(f)
			(xml, name) = newXML(l, r)
			fName = (name + "_ann")
			fileName = fName + '.xml'
			nf = open(os.path.join("/media/DATA/AI/EAPoem/Data/Sonnets/", fileName), 'w')
			nf.write(xml)
	

if __name__ == '__main__':
	sys.exit(main(sys.argv))
