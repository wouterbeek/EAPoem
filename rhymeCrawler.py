"""
Crawler to fine rhyming words on http://rhymezone.com

Author: Eszter Fodor
Version: 05/2013
"""

import sys
import mechanize
import re
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser

def getRhymes(html):
	"""
	Constructs list with all the words that came up on the site
	"""
	return True
	
def main(args):
	"""
	Program entry point
	"""
	word = args[1]
	br = mechanize.Browser()
	link = ('http://www.rhymezone.com/r/rhyme.cgi?Word=%s&typeofrhyme=perfect&org1=syl&org2=l&org3=y' % word)
	site = br.open(link)
	html = site.read()
	home = BeautifulSoup(html)
	print home
	
	site.close()
	
if __name__ == '__main__':
	sys.exit(main(sys.argv))
