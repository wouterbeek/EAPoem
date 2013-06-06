"""
Module to annotate rhymes in Shakespeare's sonnets

Author: Eszter Fodor
Version: 06/2013
"""

import sys
import os
import re
import subprocess
import xml.etree.cElementTree as ET
from xml.dom import minidom

annotations = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


"""
GET word
	SHELL --> fgrep word from CMU
		store list
	SEARCH second word in list
"""



def readFile(title):
	"""
	Read the xml's
	"""
	splittedLines = []
	sonnet = open(os.path.join("/media/DATA/AI/EAPoem/Data/Test", title), 'r+')
	tree = ET.parse(sonnet)
	root = tree.getroot()
	for line in root.iter('line'):
		lineSplit = line.text.split(" ")
		lineSplitReversed = lineSplit[::-1]
		splittedLines.append(lineSplitReversed)
	sonnet.close()
	return splittedLines
	
				
	
def annotateRhymes():
	"""
	Annotate the rhymes
	"""
	return True
	
def main():
	"""
	Program entry point
	"""
	lines = readFile('001.xml')
	print lines

	
#if __name__ == '__main__':
#	sys.exit(main(sys.args))

if __name__ == '__main__': main()
