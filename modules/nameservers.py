from insides.colors 	import *
from insides.functions 	import write, removeHTTP, addHTTP
from dns.resolver 		import query as Nameservers

def nameServers(website):
	website = removeHTTP(website)
	res 	= Nameservers(website, 'NS')
	
	for nameservers in res:
		write(var="#", color=c, data=nameservers)