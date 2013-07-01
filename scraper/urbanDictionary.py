#title			:BIRiver.py
#descripion		:Scrapes the BusinessInsider top new "River" title
#author			:David Albertson
#date			:June 25
#usage			:python BIRiver.py
#python_version	:python 2.7.3
#==============================================================================

import sys
import urllib2

from bs4 import BeautifulSoup

#Returns a random definition
def UD():
    url = "http://www.urbandictionary.com/random.php"
    data = urllib2.urlopen(url).read()
    bs = BeautifulSoup(data)
    body = bs.find("td", {"id": "middle_column"})
    
    word = body.find("td", {"class": "word"})
    word = word.find("span").get_text().strip()
    definition = body.find("div",{"class": "definition"}).get_text().strip()
    print(word)
    print(definition)

#Returns a specific definition
def UDD(keyword):
	if(str(keyword) is None):
		keyword = "pwned"
	
	keyword = keyword.replace(" ", "+")
	url = "http://www.urbandictionary.com/define.php?term=" + str(keyword)
	data = urllib2.urlopen(url, timeout=3).read()
	bs = BeautifulSoup(data)
	body = bs.find("td", {"id": "middle_column"})
	
	word = body.find("td", {"class": "word"})
	if word is None:
		print("No definition found.")
		return

	word = word.find("span").get_text().strip()
	definition = body.find("div",{"class": "definition"}).get_text().strip()
	print(word)
	print(definition)

def main():
	UD()
	UDD("Bropocalypse")

if __name__=="__main__":
	main()