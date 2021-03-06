"""
Crawler to get the sonnets of Shakespeare from the web
and storing them in a database

Author: Eszter Fodor
"""

import sys
import mechanize
import MySQLdb
import re
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser

"""
Tags to replace in texts
"""
reps = ["<td>", "\t", "\r", "</td>"]


def getPoem(html):
	"""
	Get the poem from the website
	The structure of everywebsite is different which results in the fact that the line
	"find = str(soup.body.table.contents[3].td)" must be changed for every website
	"""
	soup = BeautifulSoup(html)

	find = str(soup.body.table.contents[3].td)
	poemSplit = find.split("<br>")
	poem = strip_tags(poemSplit)
	
	return poem
	
def strip_tags(text):
	"""
	Strip the text from the tags and replace <br /> with new line
	"""
	for line in text:
		for tag in reps:
			if tag in line:
				line = line.replace(tag, "")
				if "<br />" in line:
					line = line.replace("<br />", "\n")
	return line
	


def databaseFunction(poem, author, style):
	"""
	Insert the poem, the author and the style in the database
	"""
	db = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "test")
	cur = db.cursor() 

	if cur: 
		cur.execute("INSERT INTO poemhunter VALUES (NULL, %s, %s, %s)", [poem, author, style])
		db.commit()
	else:
		print "Something went wrong"

	dbClose = db.close()

def main():
	"""
	Program entry point
	"""
	br = mechanize.Browser()
	site = br.open("http://poetry.eserver.org/sonnets/")
	html = site.read()
	home = BeautifulSoup(html)
	
	links = home.body.tt
	for al in links.findAll('a', href=True):
		newLink = br.open("http://poetry.eserver.org/sonnets/" + str(al['href']))
		htmlNew = newLink.read()
		poems = getPoem(htmlNew)
		databaseFunction(poems, "William Shakespeare", "sonnet")
	site.close()

if __name__ == '__main__': main()









