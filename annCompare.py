import signal
import sys
import os
import re
import time
import xml.etree.cElementTree as ET
from xml.dom import minidom
import xml

totalLines = 0
annLines = 0

def compare(firstFile, secondFile):
	firstTree = ET.parse(firstFile)
	firstRoot = firstTree.getroot()
	global totalLines
	global annLines
	secondTree = ET.parse(secondFile)
	secondRoot = secondTree.getroot()
	
	fileAnnLines = 0
	
	for lines in firstRoot.iter('line'):
		totalLines += 1
		try:
			for p in lines.iter('phoneme'):
				annLines += 1
		except:
			print "Nope"
		
def main(args):
	for fileName in args[1:]:
		for fileTwo in args[2:]:
			with open(fileName) as f and open(fileTwo) as f2:
				compare(f, f2)
	percentage = ((float(annLines)/totalLines)*100)
	print percentage
			
if __name__ == '__main__':
	sys.exit(main(sys.argv))
