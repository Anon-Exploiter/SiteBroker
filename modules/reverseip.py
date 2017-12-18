from bs4 import BeautifulSoup
from insides.colors import *
from insides.functions import _headers, write, Request, removeHTTP, addHTTP
import re, os
import requests

def reverseViaHT(website):
	website = addHTTP(website); webs = removeHTTP(website)
	url = "http://api.hackertarget.com/reverseiplookup/?q="
	combo = "{url}{website}".format(url=url, website=webs)
	request = Request(combo, _timeout=5, _encode=True)
	if len(request) != 5:
		list = request.strip("").split("\n")
		for _links in list:
			if len(_links) != 0:
				write(var="#", color=c, data=_links)
	else:
		write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")
