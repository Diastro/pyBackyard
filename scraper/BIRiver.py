#title			:BIRiver.py
#descripion		:Scrapes the BusinessInsider top new "River" title
#author			:David Albertson
#date			:June 25
#usage			:python BIRiver.py
#python_version	:python 2.7.3
#==============================================================================

#Module import
import sys
import urllib2

from bs4 import BeautifulSoup

def main():
		#WebRequest - data parsing
        url = "http://www.businessinsider.com"
        data = urllib2.urlopen(url).read()
        bs = BeautifulSoup(data)

        #Extracting the titles
        stories = bs.find("div", {"class": "river"})
        titles = stories.find_all("a", {"class": "title"})
        for title in titles:
                print(title.get_text().encode('ascii', 'ignore'))

if __name__=="__main__":
        main()