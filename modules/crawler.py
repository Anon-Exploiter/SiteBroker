"""
_______________.___.
\______   \__  |   |
 |    |  _//   |   |
 |    |   \\____   |
 |______  // ______|
        \/ \/       
   _____         _______           ________        __________.__         ._____________   __________ 
  /  _  \   ____ \   _  \   ____   \_____  \___  __\______   |  |   ____ |__\__    _______\______   \
 /  /_\  \ /    \/  /_\  \ /    \    _(__  <\  \/  /|     ___|  |  /  _ \|  | |    |_/ __ \|       _/
/    |    |   |  \  \_/   |   |  \  /       \>    < |    |   |  |_(  <_> |  | |    |\  ___/|    |   \
\____|__  |___|  /\_____  |___|  / /______  /__/\_ \|____|   |____/\____/|__| |____| \___  |____|_  /
        \/     \/       \/     \/         \/      \/                                     \/       \/ 

                                ~ Changing Coder Name Wont Make You One :)
                                             ~ An0n 3xPloiTeR :)
"""

from insides.colors 	import *
from bs4 				import BeautifulSoup
from insides.functions 	import _headers, write, Request, removeHTTP, addHTTP
import re, 		 os
import requests, json

def googleCrawl(website):
	search = ("site:" + str(removeHTTP(website)))
	webs = removeHTTP(website)
	for loop in range(0,10):
		url = "https://google.com/search?q=" + str(search) + "&ie=utf-8&oe=utf-8&aq=t&start=" + str(loop) + "0"
		request = requests.get(url, headers=_headers)
		content = request.text.encode('UTF-8')
		soup = BeautifulSoup(content, 'lxml')
		sub_links = soup.find_all('div', class_='r')
		for links in sub_links:
			links = links.a['href']
			if str(webs) in links:
				write(var="~", color=c, data=links)

def bingCrawl(website):
	search = ("site:" + str(removeHTTP(website)))
	webs = removeHTTP(website)
	link = []
	for loop in range(0,50):
		url = "http://www.bing.com/search?q=" + str(search) + "&first=" + str(loop) + "0"
		try:
			request = requests.get(url, headers=_headers)
			content = request.text.encode('UTF-8')
			# print(content)
			links = re.findall(r'<a\shref="(.*?)"\sh="(.*?)">', content)[5]
			# print(links[0])
			link.append(links[0])
		except requests.exceptions.ConnectionError as e:
			pass

	_link = set(link)
	for links in _link:
		if str(webs) in links:
			write(var="~", color=g, data=links)

def manualCrawl(website):
	website = addHTTP(website)
	webs = removeHTTP(website)
	request = Request(website, _timeout=5, _encode=True)
	soup = BeautifulSoup(request, 'lxml')
	### Links are in ['a', 'link', 'img', 'svg', 'iframe', 'embed', 'audio']

	_links = []

	a = soup.find_all("a")
	for links in a:
		_links.append(links['href'])

	link = soup.find_all("link")
	for links in a:
		_links.append(links['href'])

	img = soup.find_all("img")
	for links in img:
		_links.append(links['src'])

	iframe = soup.find_all("iframe")
	for links in iframe:
		_links.append(links['src'])

	embed = soup.find_all("embed")
	for links in embed:
		_links.append(links['src'])
	
	_links = set(_links)
	for __links in _links:
		if str(webs) in __links:
			write(var="~", color=c, data=__links)
