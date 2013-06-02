"""
Tool to tag the meter of Shakespearean sonnets
Fairly brute force but necessery
Idea drawn from the paper of E. Greene, T. Bodrumlu and K. Knight:
	Automatic Analysis of Rhythmic Poetry with Applications to Generation and Translation


Author: Eszter Fodor
Version: 06/2013
"""

import os
import re
import sys
import xml.etree.cElementTree as ET
import xml
import nltk
from xml.dom import minidom
from HTMLParser import HTMLParser
from xml.sax.saxutils import unescape

from nltk.corpus import cmudict

d = cmudict.dict()
def nsyl(word):
  print [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]] 
  

def main(args):
	for i in range(len(args)):
		nsyl(args[i+1])
	

if __name__ == '__main__':
	sys.exit(main(sys.argv))
	
