#title          :basicCrawler.py
#descripion     :Scrapes url from the originDomain and crawls that list of domain
#author         :David Albertson
#date           :June 30
#usage          :python basicCrawler.py
#requirements   :BeautifulSoup
#python_version :python 2.7.3
#==============================================================================

import sys
import urllib2
import string
import signal
import time
import traceback

from bs4 import BeautifulSoup

def trunc_at(s, d, n=3):
    return d.join(s.split(d)[:n])

def signal_handler(signal, frame):
    print("ByeBye")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    originDomain = "https://news.ycombinator.com/newest"
    domainSpecificScraping = 0
    urlDump = 0
    url = [originDomain]

    for urlToConsume in url:
        print("Consuming(" + str(len(url)) + "): " + urlToConsume)
        currentDomain = trunc_at(urlToConsume, "/")

        try:
            #Web request
            start_time = time.time()
            data = urllib2.urlopen(urlToConsume, timeout=3).read()
            urlRequestTime = time.time() - start_time
            print("Request time: " + str(urlRequestTime))

            #BeautifulSoup parsing
            start_time = time.time()
            bs = BeautifulSoup(data)
            bsParsingTime = time.time() - start_time
            print("BS parsing time: " + str(bsParsingTime))

            #Gets all the URL from requested URL
            links = bs.find_all('a')
            links = [s.get('href') for s in links]
            links = [str(s).strip().encode('ascii', 'ignore') for s in links]
            links = [s for s in links if s.startswith("http:") or s.startswith("https:")]
            links = [s for s in links if not s.endswith(".mp4") or s.endswith(".mp3") or s.endswith(".jpg")]
            foundUrl = set(links)

            #Rules
            if(domainSpecificScraping):
                links = [s for s in links if s.startswith(originDomain)]

            #Adds the found URL set to the URL to visit list
            url += set(links)
            set(url)

            #Dumps found URLs in .txt
            #Not efficient but does the job.
            if(urlDump):
                with open("Urls.txt", 'a') as outf:
                    outf.write('\n'.join(url))

        #Catch the Ctrl-C to exit
        except SystemExit:
            sys.exit(0)
            break

        #Catch other exceptions (timeouts, encoding, etc)
        except:
            traceback.print_exc(file=sys.stdout)
            print("Error : " + urlToConsume + " - ",  sys.exc_info()[0], sys.exc_info()[1])

if __name__=="__main__":
    main()