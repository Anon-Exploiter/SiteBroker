from insides.colors 	import *
from insides.functions 	import _headers, write, Request, removeHTTP, addHTTP
from requests 			import get

def grabBanner(website):
	website 	= addHTTP(website)
	request 	= get(website, timeout=5, headers=_headers).headers.items()

	for headers in request:
		res 	= f"{headers[0]}: {headers[1]}"
		write(var="#", color=c, data=res)