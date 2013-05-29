"""
Module to annotate rhymes in Shakespeare's sonnets

Author: Eszter Fodor
Version: 05/2013
"""

import sys
import os
import re
import xml.etree.cElementTree as ET
from xml.dom import minidom

annotations = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def readFile(title):
	"""
	Read the xml's
	"""
	splittedLines = []
	sonnet = open(os.path.join("/media/DATA/AI/EAPoem/Data/Sonnets", title), 'r+')
	tree = ET.parse(sonnet)
	root = tree.getroot()
	for line in root.iter('line'):
		lineSplit = line.text.split(" ")
		lineSplitReversed = lineSplit[::-1]
		splittedLines.append(lineSplitReversed)
	sonnet.close()
	return splittedLines
	
	
def findRhymes(splittedLines):
	"""
	Find rhyming words in the xml
	"""
	dictionary = open("dictionary_without_stress.txt", 'r')
	lists = dictionary.read()
	print lists
	lasts = []
	for lines in splittedLines:
		last = lines[0] # Last words of every line
		# Add last words to list
		lasts.append(last)
		
	for words in lasts:
		if words == lists[0][0]:
			print words
		else:
			print lists[0][0]
			
			
	
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
	findRhymes(lines)
	
#if __name__ == '__main__':
#	sys.exit(main(sys.args))

if __name__ == '__main__': main()
