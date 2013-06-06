"""
Module to automatically annotate rhymes in Shakespeare's sonnets

Author: Eszter Fodor
Version: 06/2013
"""

import sys
import os
import re
import subprocess
import xml.etree.cElementTree as ET
from xml.dom import minidom
import time

annotations = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
annotationDict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g'}

rep = ["[", " '", "]", "'", "\n", "(1)", "(2)", "(3)"]

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
	for line in root.iter('text'):
		lineSplit = line.text.split(" ")
		lineSplitReversed = lineSplit[::-1]
		splittedLines.append(lineSplitReversed)
	sonnet.close()
	return splittedLines
	

def checkRhyme(sonnet):
	lastWordsList = [] # List with all the last words of the sonnet
	restList = []
	for line in sonnet:
		lastWord = line[0]
		lastWordsList.append(lastWord.upper())
	
	# Get the primary word
	for word in lastWordsList: 
		arg = ("['"  + word.upper() + "', ") # "['WET', "
		rhymes = subprocess.check_output(["fgrep", arg, "/media/DATA/AI/Scriptie/Dictionaries/new_cmu.txt"], stderr=subprocess.STDOUT)
		rhymesList = rhymes.split(",")
		primary = rhymesList[0] # Word to search rhyme for
		for tag in rep:
			if tag in primary:
				primary = primary.replace(tag, "")
				
		# Get the list of the words that rhyme with primary		
		for i in range(1,len(rhymesList)):
			w = rhymesList[i]
			for tag in rep:
				if tag in w:
					w = w.replace(tag, "")
			restList.append(w)
		
		annotateRhymes(lastWordsList, primary, restList)
			
		
				
	
def annotateRhymes(endings, primaryWord, rhymeList):
	"""
	Annotate the rhymes
	Arguments: List with line endings, the primary word, the list the primary word rhymes with
	"""
	# Search the rhyme list for occurances
		# of the other ending words
		# If found: annotate the two words
	print primaryWord
	for end in endings:
		print end
		if ((end != primaryWord) and (end in rhymeList)):
			print '!!!!!!! yes !!!!!!'
			
		
	return True
	
def main():
	"""
	Program entry point
	"""
	begin = time.time()
	lines = readFile('Sonnet 1_meterTagged.xml')
	checkRhyme(lines)
	
	end = time.time()-begin
	print 'Time taken: %d min and %d sec' % (end/60, end%60)

	
#if __name__ == '__main__':
#	sys.exit(main(sys.args))

if __name__ == '__main__': main()
