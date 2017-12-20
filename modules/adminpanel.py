from bs4 import BeautifulSoup
from insides.colors import *
from insides.functions import _headers, write, Request, removeHTTP, addHTTP
import re, os
import requests, json

def findAdminPanel(website):
	website = addHTTP(website)
	panels = Request("https://raw.githubusercontent.com/Anon-Exploiter/Rough_Work/master/admin_panels", _timeout=6, _encode=True).split("\n")
	# website = removeHTTP(website)
	# print("{}=".format(w) * 70)
	print("{}{:<92}| {:<50}".format(c, "URL", "STATUS"))
	# print("{}=".format(w) * 70)
	for _panels in panels:
		if len(_panels) != 0:
			combo = website + "/" + _panels
			try:
				resp = requests.get(combo, timeout=5, headers=_headers).status_code
				if resp != 404:
					print("{}{:<92}| {:<50}".format(g, combo, resp))
			except Exception:
				print("{}{:<92}| {:<50}".format(r, combo, "404"))