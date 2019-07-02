"""
_______________.___.
\______   \__  |   |
 |    |  _//   |   |
 |    |   \\____   |
 |______  // ______|
        \/ \/       
   _____         _______           ________        __________.__         ._____________   __________ 
  /  _  \   ____ \   _  \   ____   \_____  \___  __\______   |  |   ____ |__\__    _______\______   \
 /  /_\  \ /    \/  /_\  \ /    \    _(__  <\  \/  /|     ___|  |  /  _ \|  | |    |_/ __ \|       _/
/    |    |   |  \  \_/   |   |  \  /       \>    < |    |   |  |_(  <_> |  | |    |\  ___/|    |   \
\____|__  |___|  /\_____  |___|  / /______  /__/\_ \|____|   |____/\____/|__| |____| \___  |____|_  /
        \/     \/       \/     \/         \/      \/                                     \/       \/ 

                                ~ Changing Coder Name Wont Make You One :)
                                             ~ An0n 3xPloiTeR :)
"""

#####################################################################################################
        ################################   Importing Packages   ################################ 
#####################################################################################################

from insides import *
from modules import BingCrawl,      browserspyRep
from modules import Cloudflare,     findSubdomains
from modules import findShells,     findAdminPanel
from modules import GoogleCrawl,    grabBanner
from modules import ManualCrawl,    nameServers
from modules import reverseViaHT,   reverseViaYGS
from modules import whoIS,          websiteSpeed

#####################################################################################################
        ################################   Variables!   ################################ 
#####################################################################################################

line        = "-" * 69
user_agent  = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"
val_Select  = f"\t{r}[$] Please Use The Index Value From The List\n\t\t[+] Not By Your Own :/\n\t\t\t ~ An0n 3xPloiTeR  \n"
str_Index   = f"\n\t{r}[=] Please Input a Integer (i.e, 1, 2, 3) :\\\n\t\t{c}~ An0n 3xPloiTeR :)"
_headers    = {
    'User-Agent': user_agent,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

#####################################################################################################
        ################################   Built-IN Functions   ################################ 
#####################################################################################################

def InDex():
    try:
        index = input(f"{c}[~] Select Any Of Thy Indexes (i.e, 1, 2, 3): "); int(index)
        return(index)
    
    except ValueError:
        exit(str_Index)

def heading(heading, website, color, afterWebHead):
    space = " " * 15
    var = str(space + heading + " '" + website + "'" + str(afterWebHead) + " ..." + space)
    length = len(var) + 1; print() # \n
    print(f"{w}" + "-" * length + "-")
    print(f"{color}" + var)
    print(f"{w}" + "-" * length + "-"); print() # \n

#####################################################################################################
        ################################   Script's Banner   ################################ 
#####################################################################################################

print(Banner)

#####################################################################################################

website = input(f"\n{b}[$] Please Enter The Website You Want To Scan {r}(i.e, hackthissite.org, hack.me): {y}"); website=addHTTP(website)

print(f"\n{g}[@] What You Wanna Do With The Given Website ? \n\n1). Cloudflare Check. \n2). Website Crawler.\n3). Reverse IP.\n4). Information Gathering.\n5). Nameservers.\n6). WebSite Speed.\n7). Subdomains Scanner.\n8). Shell Finder.\n9). Admin Panel Finder.\n10). Grab Banner.\n11). All Things.\n")

index = int(InDex())

#####################################################################################################
        ################################   Real Shit   ################################ 
#####################################################################################################

try:
    if index == 1:
        heading(heading="Checking For Cloudflare Bypass Of", website=website, afterWebHead="", color=c)
        Cloudflare(website, _verbose=True)

    elif index == 2:
        print(f"\n{b}[$] With Which Method You Wanna Crawl ?\n\n{g}1). Google Based Crawler. \n{y}2). Bing Based Crawler.\n{c}3). Manual Crawler.\n{r}4). All Things.\n")
        _index = int(InDex())

        if _index == 1:
            heading(heading="Crawling", website=website, afterWebHead=" Via Google", color=c)
            GoogleCrawl(website)

        elif _index == 2:
            heading(heading="Crawling", website=website, afterWebHead=" Via Bing (might take some time)", color=b)
            BingCrawl(website)

        elif _index == 3:
            heading(heading="Crawling", website=website, afterWebHead=" Manually :)", color=c)
            ManualCrawl(website)

        elif _index == 4:
            heading(heading="Crawling", website=website, afterWebHead=" Via Google", color=c)
            GoogleCrawl(website)

            heading(heading="Crawling", website=website, afterWebHead=" Via Bing (might take some time)", color=b)
            BingCrawl(website)

            heading(heading="Crawling", website=website, afterWebHead=" Manually :)", color=c)
            ManualCrawl(website)

        else:
            exit(val_Select)

    elif index == 3:
        print(f"\n{b}[$] With Which Method You Wanna Do Reverse IP ?\n\n{g}1). Hacker Target Based. \n{y}2). YouGetSignal Based.\n{c}3). All Things.\n")
        _index = int(InDex())

        if _index == 1:
            heading(heading="Doing Reverse IP OF", website=website, afterWebHead=" Via HT <3", color=g)
            reverseViaHT(website)

        elif _index == 2:
            heading(heading="Doing Reverse IP OF", website=website, afterWebHead=" Via YGS!", color=c)
            reverseViaYGS(website)

        elif _index == 3:
            heading(heading="Doing Reverse IP OF", website=website, afterWebHead=" Via HT <3", color=g)
            reverseViaHT(website)

            heading(heading="Doing Reverse IP OF", website=website, afterWebHead=" Via YGS!", color=c)
            reverseViaYGS(website)

        else:
            exit(val_Select)

    elif index == 4:
        print(f"\n{g}[$] With Which Method You Wanna Do Information Gathering ?\n\n{b}1). Whois Lookup. \n{y}2). BrowserSpy Report.\n{c}3). All Things.\n")
        _index = int(InDex())

        if _index == 1:
            heading(heading="Doing Whois Lookup OF", website=website, afterWebHead="", color=w)
            whoIS(website)

        elif _index == 2:
            heading(heading="Generating BrowserSpyReport Of", website=website, afterWebHead="", color=w)
            browserspyRep(website)

        elif _index == 3:
            heading(heading="Doing Whois Lookup OF", website=website, afterWebHead="", color=w)
            whoIS(website)

            heading(heading="Generating BrowserSpyReport Of", website=website, afterWebHead="", color=w)
            browserspyRep(website)

        else:
            exit(val_Select)

    elif index == 5:
        heading(heading="Finding Nameservers Of", website=website, afterWebHead="", color=w)
        nameServers(website)

    elif index == 6:
        heading(heading="Finding Loading Speed Of", website=website, afterWebHead="", color=r)
        websiteSpeed(website)

    elif index == 7:
        heading(heading="Finding SubDomains Of", website=website, afterWebHead="", color=c)
        findSubdomains(website)     

    elif index == 8:
        heading(heading="Finding Shells Of", website=website, afterWebHead="", color=c)
        findShells(website)        

    elif index == 9:
        heading(heading="Finding Admin Panel Of", website=website, afterWebHead="", color=c)
        findAdminPanel(website)

    elif index == 10:
        heading(heading="Grabbing Banner Of", website=website, afterWebHead="", color=g)
        grabBanner(website)        

    elif index == 11:
        heading(heading="Checking For Cloudflare Bypass Of", website=website, afterWebHead="", color=y)
        Cloudflare(website, _verbose=True)

        heading(heading="Crawling", website=website, afterWebHead=" Via Google", color=c)
        GoogleCrawl(website)

        heading(heading="Crawling", website=website, afterWebHead=" Via Bing (might take some time)", color=b)
        BingCrawl(website)

        heading(heading="Crawling", website=website, afterWebHead=" Manually :)", color=c)
        ManualCrawl(website)

        heading(heading="Doing Reverse IP OF", website=website, afterWebHead=" Via HT <3", color=g)
        reverseViaHT(website)

        heading(heading="Doing Reverse IP OF", website=website, afterWebHead=" Via YGS!", color=c)
        reverseViaYGS(website)

        heading(heading="Doing Whois Lookup OF", website=website, afterWebHead=" Via WApi", color=w)
        whoIS(website)

        heading(heading="Generating BrowserSpyReport Of", website=website, afterWebHead="", color=w)
        browserspyRep(website)

        heading(heading="Finding Nameservers Of", website=website, afterWebHead="", color=w)
        nameServers(website)

        heading(heading="Finding Loading Speed Of", website=website, afterWebHead="", color=r)
        websiteSpeed(website)

        heading(heading="Finding SubDomains Of", website=website, afterWebHead="", color=c)
        findSubdomains(website)

        heading(heading="Finding Shells Of", website=website, afterWebHead="", color=c)
        findShells(website)

        heading(heading="Finding Admin Panel Of", website=website, afterWebHead="", color=c)
        findAdminPanel(website)

        heading(heading="Grabbing Banner Of", website=website, afterWebHead="", color=g)
        grabBanner(website)
        
    else:
        exit(val_Select)

except KeyboardInterrupt:
    write(var="~", color=w, data="Err0r: User Interrupted!")
    
# except Exception, e:
#     write(var="#", color=r, data="Err0r: Kindly Report the err0r below to An0n3xPloiTeR :) (If Your Internet's Working ;)\n\"\"\"\n" + str(e) + "\n\"\"\"")

print(Footer)

# See Ya!
# An0n 3xPloiTeR :)