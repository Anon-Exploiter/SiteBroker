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

# from insides import Banner, Footer
from insides import *
from modules import Cloudflare
from modules import GoogleCrawl, BingCrawl, ManualCrawl
from modules import reverseViaHT, reverseViaYGS, whoIS

import re 

#####################################################################################################
        ################################   Some Errors!   ################################ 
#####################################################################################################

empty_Website = "\n{red}[=] Please Enter A Website :/\n\t{cyan}~ An0n 3xPloiTeR :)".format(red=r, cyan=c)

wrong_URL = "\n{red}[=] Please Enter a Valid And Correct URL (i.e, hackthissite.org, hack.me)\n\t{cyan}~ An0n 3xPloiTeR :)".format(red=r, cyan=c)

str_Index = "\n{red}[=] Please Input a Integer (i.e, 1, 2, 3) :\\\n\t{cyan}~ An0n 3xPloiTeR :)".format(red=r, cyan=c)

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

# website = raw_input("\n{blue}[$] Please Enter The Website You Want To Scan {red}(i.e, hackthissite.org, hack.me): ".format(blue=b, red=r)); website=addHTTP(website)

# print("\n{green}[@] What You Wanna Do With The Given Website ? \n\n1). Cloudflare Check / Bypass. \n2). Website Crawler.\n3). Reverse IP.\n4). Information Gathering.\n5). Nameservers.\n6). WebSite Speed.\n7). Subdomains Scanner.\n8). Shell Finder.\n9). Admin Panel Finder.\n10). Grab Banner.\n11). All Things.\n".format(green=g)) # Options

# index = int(InDex())

#####################################################################################################
        ################################   Real Shit   ################################ 
#####################################################################################################

# if index == 1:
#     heading(heading="Checking For Cloudflare Bypass Of", website=website, color=c)
#     Cloudflare(website)
#     print(Footer)

# heading(heading="Crawling", website="http://umarshah.tk", afterWebHead=" Via Google", color=c)
# GoogleCrawl("http://umarshah.tk")

# heading(heading="Crawling", website="http://umarshah.tk", afterWebHead=" Via Bing", color=b)
# BingCrawl("http://umarshah.tk")

# heading(heading="Crawling", website="http://umarshah.tk", afterWebHead=" Manually :)", color=c)
# ManualCrawl("http://umarshah.tk")

# heading(heading="Doing Reverse IP OF", website="http://umarshah.tk", afterWebHead=" Via YGS!", color=c)
# reverseViaYGS("http://umararfeen.com")

# heading(heading="Doing Reverse IP OF", website="http://umarshah.tk", afterWebHead=" Via HT <3", color=g)
# reverseViaHT("http://umararfeen.com")

heading(heading="Doing WhoIS OF", website="http://umararfeen.com", afterWebHead="", color=w)
whoIS("umararfeen.com")