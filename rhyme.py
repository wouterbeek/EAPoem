"""
Program to create a rhyme dictionary

To run: $ python rhyme.python english_phonetics.py

Author: Eszter Fodor
Version: 05/2013
"""

import re
import os
import sys
import itertools


def loadFile(english, output):
	"""
	Read the file and split between the words and their phonetics
	"""
	phonetics = open(english, 'r')
	out = open(output, 'w')
	buffer = phonetics.read().split('\n')
	return (buffer, out)
		

def getRhymes(loaded,out):
	"""
	Get the phonetics of every word and reverse it
	Create dictionary with every word and the ending phonetics
	"""
	for line in loaded:
		if line == '':
			break
		else:
			(word, phon) = line.split('\\')
			phonSplit = phon.split('-')
			phonReverse = phonSplit[::-1]
			line = dict([(word, phonReverse[0])])
			for key in line.keys():
				rhyme = []
				rhyme.append(key)
				keyVal = line[key]
				words = [key for key, val in line.iteritems() if val == keyVal]
				rhyme.append(words)
			out.write(str(rhyme)) 
			out.write("\n")

	
def main(args):
	"""
	Program entry point
	Argument: filename
	"""
	(load,out) = loadFile(args[1], args[2])
	getRhymes(load,out)
	
	
	
if __name__ == '__main__':
	sys.exit(main(sys.argv))
