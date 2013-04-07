"""
This will eventually be a webcrawler to get poems from poemhunter.com
At this point this is only a minimalistic crawler since this will be my first crawler

Author: Eszter Fodor
"""

import mechanize
import urllib2
from BeautifulSoup import BeautifulSoup


br = mechanize.Browser()
site = br.open("http://loremipsum.net/")
html = site.read()

soup = BeautifulSoup(html)
body = soup.body
rightTable = body.contents[1].contents[3].p

print rightTable









