"""
Program to create a rhyme dictionary from CMU dictionary
Adapted version of createRhymeDict.py

To run: $ python cmuRhyme.py cmudict.txt cmuRhymes.txt


Author: Eszter Fodor
Version: 05/2013
"""

import re
import os
import sys
import itertools
import time

rep = ["'","(1)", "(2)", "(3)"]


def loadFile(cmu, output):
	"""
	Read the file and split between the words and their phonetics
	"""
	phonetics = open(cmu, 'r')
	out = open(output, 'w')
	buffer = phonetics.read().split('\n')
	return (buffer, out)
		

def getRhymes(loaded,out):
	"""
	Get the phonetics of every word and reverse it
	Create dictionary with every word and the ending phonetics
	"""
	lines = dict([])
	# For every line in file
	for line in loaded:
		if line == '':
			break
		else:
			# Get word and phonetics
			(word, phon) = line.split('  ')
			# Replace noisy characters
			for tag in rep:
				if tag in word:
					word = word.replace(tag, "")
			phonSplit = phon.split(' ')
			phonReverse = phonSplit[::-1]
			# Add word and last part of phonetics to dictionary and consider stress
			for i in range(len(phonReverse)):
				if (str(0) in phonReverse[i] or str(1) in phonReverse[i] or str(2) in phonReverse[i]):
					if i == 0:
						lines.update({word:phonReverse[i]})
					elif i == 1:
						lines.update({word:(phonReverse[1] + phonReverse[0])})
					elif i == 2:
						lines.update({word:(phonReverse[2] + phonReverse [1] + phonReverse[0])})
			
	# For every word in dictionary
	for key in lines.keys():
		rhyme = []
		words = []
		# Add the word to list
		rhyme.append(key)
		keyVal = lines[key]
		# For every other word in the dictionary
		for keys, values in lines.items():
			# If it's value is the same as of the word
			if values == keyVal:
				# Add the word to list of words
				words.append(keys)
	
		# rhyme = list of list with [word, [rhyming words]]	
		rhyme.append(words)
		out.write(str(rhyme)) 
		out.write("\n")

	
def main(args):
	"""
	Program entry point
	Argument: filename
	"""
	begin = time.time()
	(load,out) = loadFile(args[1], args[2])
	getRhymes(load,out)
	
	end = time.time()-begin
	print 'Time taken: %d min and %d sec' % (end/60, end%60)
	
	
	
if __name__ == '__main__':
	sys.exit(main(sys.argv))
