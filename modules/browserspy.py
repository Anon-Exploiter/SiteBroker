from insides.colors 	import *
from bs4 				import BeautifulSoup
from insides.functions 	import _headers, write, Request, removeHTTP, addHTTP
import re, 		 os
import requests, json

def browserspyRep(website):
	url 	= "http://browserspy.dk/webserver.php"
	_data 	= {
		'server': removeHTTP(website)
	}
	
	request = requests.post(url, headers=_headers, data=_data).text.encode('UTF-8')
	_data 	= re.findall(r'<tr class="(.*)">\n<td class="property">(.*)</td>\n<td class="value">(.*)</td>\n</tr>', request.decode())
	
	for res in _data:
		result = res[1].capitalize() + ": " + res[2]
		write(var="#", color=c, data=result)