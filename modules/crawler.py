from bs4 import BeautifulSoup
from insides.colors import *
from insides.functions import _headers, write, Request, removeHTTP, addHTTP
import re, os
import requests

def googleCrawl(website):
	search = ("site:" + str(removeHTTP(website)))
	for loop in range(0,10):
		url = "https://google.com/search?q=" + str(search) + "&ie=utf-8&oe=utf-8&aq=t&start=" + str(loop) + "0"
		request = requests.get(url, headers=_headers, timeout=5)
		content = request.content
		soup = BeautifulSoup(content, 'lxml')
		sub_links = soup.find_all('h3', class_='r')
		for links in sub_links:
			links = links.a['href']
			write(var="~", color=g, data=links)

def bingCrawl(website):
	search = ("site:" + str(removeHTTP(website)))
	link = []
	_link = []
	_links = []
	for loop in range(0,50):
		url = "http://www.bing.com/search?q=" + str(search) + "&first=" + str(loop) + "0"
		request = requests.get(url, headers=_headers, timeout=5)
		content = request.text.encode('UTF-8')
		links = re.findall(r'<a\shref="(.*?)"\sh="(.*?)">', content)[5]
		link.append(links[0])

	_link = set(link)
	for links in _link:
		print links

def manualCrawl(website):
	website = addHTTP(website)
	request = Request(website, _timeout=5, _encode=True)
	soup = BeautifulSoup(request, 'lxml')
	### Links are in ['a', 'link', 'img', 'svg', 'iframe', 'embed', 'audio']

	_links = []

	a = soup.find_all("a")
	for links in a:
		print links['href']

	link = soup.find_all("link")
	for links in a:
		print links['href']