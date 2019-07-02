from insides.colors 	import *
from bs4 				import BeautifulSoup
from insides.functions 	import _headers, write, Request, removeHTTP, addHTTP
import re, 		 os
import requests, json

def whoIS(website):
	website 	= removeHTTP(website)
	url 		= f"https://www.whois.com/whois/{website}"
	
	try:
		request 	= Request(url, _timeout=5, _encode=None)
		bs 			= BeautifulSoup(request, 'html.parser')
		result 		= bs.find_all('pre', {'class': 'df-raw'})[0].text.encode('UTF-8')
		print(f"\r{c}{result.decode()}")
	
	except:
		write(var="!", color=r, data="Sorry, whois cannot be performed right now...!!! :[")


## Lazy to add a new API key. So, added an good alternate method above! xD
## Old Code can be found below!
# website = "http://api.whoapi.com/?apikey=66ca3039356c0287ff63ed472f528478&r=whois&domain={url}&ip=".format(url=website)
# req = Request(website, _timeout=8, _encode=True)
# js = json.loads(req)
# whois = js['whois_raw']
# for result in whois.split("\n"):
# 	if len(result) != 0:
# 		write(var="~", color=c, data=result)
