from bs4 import BeautifulSoup
import urllib2
import time

def parse(url):
	try:
		ts = str(time.time())
		filename = ts+".html"
		hdr = {'User-Agent': 'Mozilla/5.0'}
		req = urllib2.Request(url,headers=hdr)
		url = urllib2.urlopen(req)
		url_read = url.read()
		url.close()
		fopen = open(filename,'w')
		soup = BeautifulSoup(url_read,"lxml")
		fopen.write('<head>''\n''<link rel="stylesheet" type="text/css" href="style.css">''\n''</head>''\n')
		for link in soup.find_all(['p','h1','h2','pre']):
			data = link.encode('utf-8')
			fopen.write(data)
			fopen.write("<br>")

		fopen.close()
	except Exception as e:
		print e

parse("http://fossbytes.com/atoms-shriek-inside-the-fusion-reactor-shows-mit/")
