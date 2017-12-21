from bs4 import BeautifulSoup
from insides.colors import *
from insides.functions import _headers, write, Request, removeHTTP, addHTTP
import re, os
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