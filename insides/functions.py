from insides.colors import *
import requests
import re

_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

empty_Website   = f"\n\t{r}[=] Please Enter A Website :/\n\t\t{c}~ An0n 3xPloiTeR :)"
wrong_URL       = f"\n\t{r}[=] Please Enter a Valid And Correct URL (i.e, hackthissite.org, hack.me)\n\t\t{c}~ An0n 3xPloiTeR :)"
str_Index       = f"\n\t{r}[=] Please Input a Integer (i.e, 1, 2, 3) :\\\n\t\t{c}~ An0n 3xPloiTeR :)"
val_Select      = f"\t{r}[$] Please Use The Index Value From The List\n\t\t[+] Not By Your Own :/\n\t\t\t ~ An0n 3xPloiTeR  \n"

def webNotEmpty(website):
    """
    Check Whether if the website is empty or not and return valid / !valid
    """
    if len(website) >= 1:
        return "valid"
    else:
        return "!valid"

def validWebsite(website):
    """
    Checks With a Regex If The URL Entered Is Correct Or Not! (User can use IP Too :)
    """
    web = webNotEmpty(website)

    if web is "valid":
        if not (re.match(r"(^(http://|https://)?([a-z0-9][a-z0-9-]*\.)+[a-z0-9][a-z0-9-]*$)", website)):
            exit(wrong_URL)
    
    else:
        exit(empty_Website)

def cleanURL(website):
    """
    Removes ["http://", "http://www.", "https://", "https://www.", "www."] from the start of the Url!
    """
    web = validWebsite(website)
    website = website.replace("http://", "")
    website = website.replace("http://www.", "")
    website = website.replace("https://", "")
    website = website.replace("https://www.", "")
    website = website.replace("www.", ""); return(website)

def removeHTTP(website):
    """
    Removes ["http://", "http://www.", "https://", "https://www.", "www."] from the start of the Url and returns it!
    """
    website = cleanURL(website); return(website)

def addHTTP(website):
    """
    Removes ["http://", "http://www.", "https://", "https://www.", "www."] from the start of the Url and add a "http://" in the start again and return it!
    """
    website = cleanURL(website)
    website = ("http://" + website); return(website)

def write(var, color, data):
    if var == None:
        print(f"{color}{str(data)}")

    elif var != None:
        print(f"{w}[{g}{var}{w}]{color} {str(data)}")

def Request(website, _timeout=None, _encode=None):
    """
    For Getting The Page Source || Source Code Of The Website Given.
    """

    try:
        if _encode == None:
            return requests.get(website, headers=_headers, timeout=_timeout).content

        elif _encode == True:
            return requests.get(website, headers=_headers, timeout=_timeout).text.encode('utf-8')

    except requests.exceptions.MissingSchema:
        pass

    except requests.exceptions.ContentDecodingError:
        pass

    except requests.exceptions.ConnectionError:
        return fg + sb + "\n[$] Err0r: Sorry! You Entered A Wrong Website 0r Website Is 0ff"
        pass

    except Exception as e:
        return fc + sb + "[$] Err0r: " + fg + sb + str(e)
        pass