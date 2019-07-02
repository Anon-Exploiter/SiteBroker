import requests, re
from insides.colors import *
from insides.functions import _headers, write, Request

def cloudflare(website, _verbose=None):
    if _verbose != None:
        write(var="#", color=c, data=f"Checking for Cloudflare in {website}")

    combo = f"http://api.hackertarget.com/httpheaders/?q={str(website)}"
    request = Request(combo, _timeout=3, _encode=True).decode()

    if "cloudflare" in request:
        write(var="~", color=g, data="Cloudflare Found!\n")

    else:
        if _verbose != None:
            write(var="^", color=g, data=f"{website} is not using Cloudflare!")