import requests, re
from insides.colors import *
from insides.functions import _headers, write, Request, addHTTP
import socket, time, urllib, urlparse, optparse

def websiteSpeed(website):
    website = addHTTP(website)
    urlinfo = urlparse.urlparse(website)

    start = time.time()
    ip = socket.gethostbyname( urlinfo.netloc )
    dns_tm = time.time()-start
    _dns = "{:<10}:{:>40} seconds".format(" DNS", dns_tm )
    write(var="~", color=g, data=_dns)

    start = time.time()
    _data = urllib.urlopen(website).read()
    load_tm = time.time()-start
    _load = "{:<10}:{:>40} seconds".format(" Load", load_tm )
    _wo = "{:<10}:{:>40} seconds".format(" W/O DNS", load_tm-dns_tm )
    
    write(var="#", color=c, data=_load)
    write(var="~", color=g, data=_wo)