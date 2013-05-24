"""
Program to create a rhyme dictionary

To run: $ python rhyme.python english_phonetics.py

Author: Eszter Fodor
Version: 05/2013
"""

import re
import os
import sys

def loadFile(filename):
	"""
	Read the file and split between the words and their phonetics
	"""
	file = open(filename, 'r')
	file.split('\n')

def getRhymes(phonetics):
	phonSplit = phonetics.split('-')
	phonReverse = phonSplit.reverse()
	print phonReverse
	
	
	
def main(args):
	"""
	Program entry point
	Argument: filename
	"""
	load = loadFile(args[1])
	#for line in load:
		#print line
	
	
if __name__ == '__main__':
	sys.exit(main(sys.argv))
