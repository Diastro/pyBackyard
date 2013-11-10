import urlparse
import urllib2
import sys
from bs4 import BeautifulSoup

# static list
# url = ['http://www.vimeo.com', \
# 	'http://www.google.com', \
# 	'http://www.youtube.com', \
# 	'http://www.kijiji.com',
# 	'http://www.businessinsider.com', \
# 	'http://www.github.com', \
# 	'http://www.nytimes.com', \
# 	'http://www.ebay.com',
# 	'http://www.paypal.com', \
# 	'http://www.wikipedia.com', \
# 	'http://www.reddit.com']

# dynamic list
urls = []
file = open('domain.txt', 'r')
for url in file:
    url = "".join(url.split()).replace(",","")
    urls.append(url)

for u in urls:
	try :
		u = "http://" + u
		AGENT_NAME = '*'
		robotURL = urlparse.urljoin(u, 'robots.txt')

		request = urllib2.Request(robotURL)
		request.add_header('User-agent', 'Zeek-BotExperiment')
		data = urllib2.urlopen(request,  timeout=4)

		bs = BeautifulSoup(data)
		robot = bs.find('p')

		for line in robot.getText().split('\n'):
			if "User-agent" in line:
				if '*' not in line:
					print line

	except KeyboardInterrupt:
		sys.exit()

	except:
		print "Skipping: " + u
		continue

