from insides.colors     import *
from insides.functions  import _headers, write, Request, addHTTP
import requests, re
import socket, time, optparse
from urllib.parse import urlparse
from urllib.request import urlopen

def websiteSpeed(website):
    website = addHTTP(website)
    urlinfo = urlparse(website)

    start   = time.time()
    ip      = socket.gethostbyname( urlinfo.netloc )
    dns_tm  = time.time()-start
    _dns    = "{:<10}:{:>40} seconds".format(" DNS", dns_tm )
    write(var="~", color=g, data=_dns)

    start   = time.time()
    _data   = urlopen(website).read()
    load_tm = time.time()-start
    _load   = "{:<10}:{:>40} seconds".format(" Load", load_tm )
    _wo     = "{:<10}:{:>40} seconds".format(" W/O DNS", load_tm-dns_tm )
    
    write(var="#", color=c, data=_load)
    write(var="~", color=g, data=_wo)