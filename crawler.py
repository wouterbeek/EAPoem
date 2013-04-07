"""
This will eventually be a webcrawler to get poems from poemhunter.com
At this point this is only a minimalistic crawler since this will be my first crawler

Author: Eszter Fodor
"""

import mechanize
import MySQLdb
from BeautifulSoup import BeautifulSoup


br = mechanize.Browser()
site = br.open("http://loremipsum.net/")
html = site.read()

soup = BeautifulSoup(html)
body = soup.body
lorem = str(body.contents[1].contents[3].p)
loremSplit = lorem.split("<p>")
loremRight = loremSplit[1]

db = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "test")
cur = db.cursor() 

if cur: 
	cur.execute("INSERT INTO poemhunter VALUES (4, %s, 'test1', 'test2')", loremRight)
	db.commit()
else:
	print "Something went wrong"

dbClose = db.close()











