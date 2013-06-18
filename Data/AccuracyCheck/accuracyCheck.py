"""
Automatic rhyme annotation and checking accuracy of it

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
from xml.sax.saxutils import unescape

annotations = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

rep = ["[", " '", "]", "'", "\n", "(1)", "(2)", "(3)"]

def readFile(title):
	"""
	Read the xml's
	Argument: file name
	"""
	splittedLines = []
	sonnet = open(os.path.join("/media/DATA/AI/EAPoem/Data/AccuracyCheck", title), 'r+')
	tree = ET.parse(sonnet)
	root = tree.getroot()
	for line in root.iter('line'):
		lineSplit = line.text.split(" ")
		lineSplitReversed = lineSplit[::-1]
		splittedLines.append(lineSplitReversed)
	sonnet.close()
	return splittedLines, root
	

def checkRhyme(sonnet, root):
	"""
	Look for rhymes in the sonnet
	Arguments: reversed splitted lines of the sonnet, xml root
	"""
	# Create a list with the last words of the lines of the sonnet
	lastWordsList = [] 
	restList = []
	for line in sonnet:
		lastWord = line[0]
		lastWordsList.append(lastWord.upper())
	
	flag = 0
	# For every word in the list of last words...
	while ((lastWordsList != []) and (flag < len(lastWordsList))): 
		word = lastWordsList[flag]
		print word
		arg = ("['"  + word.upper() + "', ") # "['WET', "
		
		# ...look for that word in de rhyme dictionary...
		try:
			rhymes = subprocess.check_output(["fgrep", arg, "/media/DATA/AI/Scriptie/Dictionaries/new_cmuV3.txt"], stderr=subprocess.STDOUT)
			# Returns a string
		except KeyboardInterrupt:
			sys.exit(0)
		except:
			print 'poep'
			flag = flag + 1
			pass
		
		# ...if found, split the string, thus creating a list...
		rhymesList = rhymes.split(",")
		primary = rhymesList[0] # ...The first word is the primary word...
		
		# Replace noisy characters
		for tag in rep:
			if tag in primary:
				primary = primary.replace(tag, "")
				
		# ...Get the list of the words that rhyme with primary...
		for i in range(1,len(rhymesList)):
			w = rhymesList[i]
			for tag in rep:
				if tag in w:
					w = w.replace(tag, "")
			restList.append(w)
		
		# ...Search for a match within the rhymes...
		end = annotateRhymes(lastWordsList, primary, restList, sonnet, root)
		restList = []
		
		# If rhymes found, delete the words from the list of last words
		if (end != None):
			lastWordsList.remove(primary)
			lastWordsList.remove(end)
		else:
			flag = flag + 1
			
	
				
def annotateRhymes(endings, primaryWord, rhymeList, rev, root):
	"""
	Annotate the rhymes
	Arguments: list with line endings, the primary word, the list the primary word rhymes with
	"""
	for end in endings:
		#print primaryWord

		if ((end != primaryWord) and (end in rhymeList)):	
			ann = annotations[0]
			newPrimary = ("<" + ann + ">" + primaryWord.lower() + "</" + ann + ">")	
			newEnd = ("<" + ann + ">" + end.lower() + "</" + ann + ">")	
			print newPrimary
			print newEnd
			annotations.remove(ann)	
			#replaceEnding(primaryWord, end, newPrimary, newEnd, rev, root)
			return end 
	


def prettify(elem):
    """
    Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    r = rough_string.replace("  ", "")
    reparsed = minidom.parseString(r)
    return reparsed.toprettyxml(indent="  ")

		

def main():
	"""
	Program entry point
	"""
	begin = time.time()
	(lines, root)= readFile('005.xml')
	checkRhyme(lines, root)
	
	end = time.time()-begin
	print 'Time taken: %d min and %d sec' % (end/60, end%60)

	
#if __name__ == '__main__':
#	sys.exit(main(sys.args))

if __name__ == '__main__': main()
	

	



