from insides.colors 	import *
from bs4 				import BeautifulSoup
from insides.functions 	import _headers, write, Request, removeHTTP, addHTTP
import re, 		 os
import requests, json

def reverseViaHT(website):
	website = addHTTP(website)
	webs 	= removeHTTP(website)

	url 	= "http://api.hackertarget.com/reverseiplookup/?q="
	combo 	= f"{url}{webs}"
	request = Request(combo, _timeout=5, _encode=True)
	
	if len(request) != 5:
		list = request.decode().strip("").split("\n")
		
		for _links in list:
			if len(_links) != 0:
				write(var="#", color=c, data=_links)

	else:
		write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def reverseViaYGS(website):
	website = addHTTP(website)
	webs 	= removeHTTP(website)
	
	url 	= "https://domains.yougetsignal.com/domains.php"
	post 	= {
        'remoteAddress' : webs,
        'key' : ''
    }

	request = requests.post(url, headers=_headers, data=post)
	request = request.text.encode('UTF-8')

	grab	= json.loads(request)
	# print(grab)
	Status 			= grab['status']
	IP 				= grab['remoteIpAddress']
	Domain 			= grab['remoteAddress']
	Total_Domains 	= grab['domainCount']
	Array 			= grab['domainArray']

	if (Status == 'Fail'):
		write(var="#", color=r, data="Sorry! Reverse Ip Limit Reached.")
	
	else:
		write(var="$", color=c, data=f"IP: {IP}")
		write(var="$", color=c, data=f"Domain: {Domain}")
		write(var="$", color=c, data=f"Total Domains: {Total_Domains}\n")

		domains = []

		for x, y in Array:
		    domains.append(x)

		for res in domains:
			write(var="#", color=b, data=res)