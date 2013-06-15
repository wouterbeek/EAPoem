"""
Crawler to fine rhyming words on http://rhymezone.com

Author: Eszter Fodor
Version: 05/2013

!!! NOTE: Uncomplete !!!
"""

# regex: <a class="d" href="d=*"> ... </a> || <a href="d=*"> ... </a>

import sys
import mechanize
import re
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser

def getRhymes(html):
	"""
	Constructs list with all the words that came up on the site
	"""
	soup = BeautifulSoup(html)
	find = soup.body.center.center
	b = find.findAll('a', href = True,text=True)
	print b


	#rhymes = find.findAll('a', href = True)
	#print rhymes
	
def main(args):
	"""
	Program entry point
	Argument: word to look up
	"""
	word = args[1]
	br = mechanize.Browser()
	link = ('http://www.rhymezone.com/r/rhyme.cgi?Word=%s&typeofrhyme=perfect&org1=syl&org2=l&org3=y' % word)
	site = br.open(link)
	html = site.read()
	getRhymes(html)
	
	site.close()
	
if __name__ == '__main__':
	sys.exit(main(sys.argv))
