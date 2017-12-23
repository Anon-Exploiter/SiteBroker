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

from insides.colors 	import *
from bs4 				import BeautifulSoup
from insides.functions 	import _headers, write, Request, removeHTTP, addHTTP
import re, 		 os
import requests, json

def findShells(website):
	website = addHTTP(website)
	shells = Request("https://raw.githubusercontent.com/Anon-Exploiter/Rough_Work/master/shells", _timeout=6, _encode=True).split("\n")
	print("{}{:<92}| {:<50}".format(c, "URL", "STATUS"))
	for _shells in shells:
		if len(_shells) != 0:
			combo = website + "/" + _shells
			try:
				resp = requests.get(combo, timeout=5, headers=_headers).status_code
				if resp != 404:
					print("{}{:<92}| {:<50}".format(g, combo, resp))
				else:
					print("{}{:<92}| {:<50}".format(r, combo, "404"))
			except Exception:
				print("{}{:<92}| {:<50}".format(r, combo, "404"))