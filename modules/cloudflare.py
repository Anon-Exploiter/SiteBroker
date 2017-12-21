import requests, re
from insides.colors import *
from insides.functions import _headers, write, Request

def cloudflare(website, _verbose=None):
    if _verbose != None:
        write(var="#", color=c, data="Checking For Cloudflare In " + website)
    combo = ("http://api.hackertarget.com/httpheaders/?q=" + str(website))
    request = Request(combo, _timeout=3, _encode=True)
    if "cloudflare" in request:
        if _verbose != None:
            write(var="~", color=g, data="Cloudflare Found!\n")
            write(var="#", color=y, data="Trying To Bypass Cloudflare!\n")
        req = "http://www.crimeflare.biz/cgi-bin/cfsearch.cgi"
        pos = {'cfS': website}
        res = requests.post(req, headers=_headers, data=pos).text.encode('utf-8')
        real_ip = None
        if re.findall(r'\d+\.\d+\.\d+\.\d+', res):
            reg = re.findall(r'\d+\.\d+\.\d+\.\d+', res)
            real_ip = reg[1]
        else:
            write(var="!", color=r, data="Sorry! Cloudflare Wasn't Bypassed :')")
        request = Request("http://" + str(real_ip), _timeout=3, _encode=True)
        if not "cloudflare" in request.lower():
            if _verbose != None:
                if real_ip != None:
                    write(var="@", color=c, data="Cloudflare Bypassed!")
                    write(var="~", color=g, data="Real IP --> " + fc +str(real_ip))
            return(str(real_ip))
        else:
            if _verbose != None:
                write(var="!", color=r, data="Sorry! Cloudflare Wasn't Bypassed :')")
    else:
        if _verbose != None:
            write(var="$", color=b, data=website + " Is not using Cloudflare!")

# cloudflare("http://mukarramkhalid.com")