"""
Extrancting only the words from CMU phonetics
"""

import os
import sys
import os
import re
import time
import itertools

rep = ["'","(1)", "(2)", "(3)", "."]

def get_words(fromFile, toFile):
	reading = open(fromFile, 'r')
	writing = open(toFile, 'w')
	
	buffer = reading.read().split('\n')
	
	for line in buffer:
		if line == '':
			break
		else:
			word = line.split(' ')[0]
			for tag in rep:
				if tag in word:
					word = word.replace(tag, "")
			wordLower = word.lower()
			writing.write(wordLower)
			writing.write(".")
			writing.write("\n")
			
def main(args):
	start = time.time()
	get_words(args[1], args[2])
	end = time.time()- start
	print 'Time taken: %d min and %d sec' % (end/60, end%60)
	
	
			
			
if __name__ == '__main__':
	sys.exit(main(sys.argv))			
			
