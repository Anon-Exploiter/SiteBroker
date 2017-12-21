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

import re

#####################################################################################################
        ################################   Some Variables!   ################################ 
#####################################################################################################

line = "-" * 69

_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"

header = {'User-Agent' : user_agent}

val_Select = "\t{}[$] Please Use The Index Value From The List\n\t\t[+] Not By Your Own :/\n\t\t\t ~ An0n 3xPloiTeR  \n".format(r)

str_Index = "\n\t{red}[=] Please Input a Integer (i.e, 1, 2, 3) :\\\n\t\t{cyan}~ An0n 3xPloiTeR :)".format(red=r, cyan=c)


#####################################################################################################
        ################################   Built-IN Functions   ################################ 
#####################################################################################################

def InDex():
    try:
        index = raw_input("{cyan}[~] Select Any Of Thy Indexes (i.e, 1, 2, 3): ".format(cyan=c)); int(index)
        return index
    except ValueError:
        exit(str_Index)

def heading(heading, website, color, afterWebHead):
    space = " " * 15
    var = str(space + heading + " '" + website + "'" + str(afterWebHead) + " ..." + space)
    length = len(var) + 1; print "" # \n
    print("{white}" + "-" * length + "-").format(white=w)
    print("{color}" + var).format(color=color)
    print("{white}" + "-" * length + "-").format(white=w); print "" # \n

#####################################################################################################
        ################################   Script's Banner   ################################ 
#####################################################################################################

print(Banner)

#####################################################################################################

website = raw_input("\n{blue}[$] Please Enter The Website You Want To Scan {red}(i.e, hackthissite.org, hack.me): ".format(blue=b, red=r)); website=addHTTP(website)

print("\n{green}[@] What You Wanna Do With The Given Website ? \n\n1). Cloudflare Check / Bypass. \n2). Website Crawler.\n3). Reverse IP.\n4). Information Gathering.\n5). Nameservers.\n6). WebSite Speed.\n7). Subdomains Scanner.\n8). Shell Finder.\n9). Admin Panel Finder.\n10). Grab Banner.\n11). All Things.\n".format(green=g)) # Options

index = int(InDex())

#####################################################################################################
        ################################   Real Shit   ################################ 
#####################################################################################################

try:
    if index == 1:
        heading(heading="Checking For Cloudflare Bypass Of", website=website, afterWebHead="", color=c)
        Cloudflare(website, _verbose=True)
        print(Footer)

    elif index == 2:
        print("\n{}[$] With Which Method You Wanna Crawl ?\n\n{}1). Google Based Crawler. \n{}2). Bing Based Crawler.\n{}3). Manual Crawler.\n{}4). All Things.\n".format(b, g, y, c, r))
        _index = int(InDex())

        if _index == 1:
            heading(heading="Crawling", website=website, afterWebHead=" Via Google", color=c)
            GoogleCrawl(website)
            print(Footer)

        elif _index == 2:
            heading(heading="Crawling", website=website, afterWebHead=" Via Bing", color=b)
            BingCrawl(website)
            print(Footer)

        elif _index == 3:
            heading(heading="Crawling", website=website, afterWebHead=" Manually :)", color=c)
            ManualCrawl(website)
            print(Footer)

        elif _index == 4:
            heading(heading="Crawling", website=website, afterWebHead=" Via Google", color=c)
            GoogleCrawl(website)

            heading(heading="Crawling", website=website, afterWebHead=" Via Bing", color=b)
            BingCrawl(website)

            heading(heading="Crawling", website=website, afterWebHead=" Manually :)", color=c)
            ManualCrawl(website)
            print(Footer)

        else:
            exit(val_Select)

    elif index == 3:
        print("\n{}[$] With Which Method You Wanna Do Reverse IP ?\n\n{}1). Hacker Target Based. \n{}2). YouGetSignal Based.\n{}3). All Things.\n".format(b, g, y, c))
        _index = int(InDex())

        if _index == 1:
            heading(heading="Doing Reverse IP OF", website=website, afterWebHead=" Via HT <3", color=g)
            reverseViaHT(website)
            print(Footer)

        elif _index == 2:
            heading(heading="Doing Reverse IP OF", website=website, afterWebHead=" Via YGS!", color=c)
            reverseViaYGS(website)
            print(Footer)

        elif _index == 3:
            heading(heading="Doing Reverse IP OF", website=website, afterWebHead=" Via HT <3", color=g)
            reverseViaHT(website)

            heading(heading="Doing Reverse IP OF", website=website, afterWebHead=" Via YGS!", color=c)
            reverseViaYGS(website)
            print(Footer)

        else:
            exit(val_Select)

    elif index == 4:
        print("\n{}[$] With Which Method You Wanna Do Information Gathering ?\n\n{}1). Whois Lookup. \n{}2). BrowserSpy Report.\n{}3). All Things.\n".format(g, b, y, c))
        _index = int(InDex())

        if _index == 1:
            heading(heading="Doing Whois Lookup OF", website=website, afterWebHead=" Via WApi", color=w)
            whoIS(website)
            print(Footer)

        elif _index == 2:
            heading(heading="Generating BrowserSpyReport Of", website=website, afterWebHead="", color=w)
            browserspyRep(website)
            print(Footer)

        elif _index == 3:
            heading(heading="Doing Whois Lookup OF", website=website, afterWebHead=" Via WApi", color=w)
            whoIS(website)

            heading(heading="Generating BrowserSpyReport Of", website=website, afterWebHead="", color=w)
            browserspyRep(website)
            print(Footer)

        else:
            exit(val_Select)

    elif index == 5:
        heading(heading="Finding Nameservers Of", website=website, afterWebHead="", color=w)
        nameServers(website)
        print(Footer)

    elif index == 6:
        heading(heading="Finding Loading Speed Of", website=website, afterWebHead="", color=r)
        websiteSpeed(website)
        print(Footer)

    elif index == 7:
        heading(heading="Finding SubDomains Of", website=website, afterWebHead="", color=c)
        findSubdomains(website)
        print(Footer)

    elif index == 8:
        heading(heading="Finding Shells Of", website=website, afterWebHead="", color=c)
        findShells(website)
        print(Footer)

    elif index == 9:
        heading(heading="Finding Admin Panel Of", website=website, afterWebHead="", color=c)
        findAdminPanel(website)
        print(Footer)

    elif index == 10:
        heading(heading="Grabbing Banner Of", website=website, afterWebHead="", color=g)
        grabBanner(website)
        print(Footer)

    elif index == 11:
        heading(heading="Crawling", website=website, afterWebHead=" Via Google", color=c)
        GoogleCrawl(website)

        heading(heading="Crawling", website=website, afterWebHead=" Via Bing", color=b)
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
        print(Footer)
        
    else:
        exit(val_Select)

except KeyboardInterrupt:
    write(var="~", color=w, data="Err0r: User Interrupted!")
    print(Footer)

except Exception, e:
    write(var="#", color=r, data="Err0r: Kindly Report This err0r to An0n3xPloiTeR :) (If Your Internet's Working ;)\n" + str(e))
    print(Footer)