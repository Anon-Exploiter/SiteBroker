#!/usr/bin/python

import optparse
import urllib2
import time
import sys

flag = 0 # A Flag to varify if no admin panel found
banner = ''''''
sap = "-" * 69

def urlFix(url): #Fix URL if http or https missing
        if "http://" in url or "https://" in url:
                return url

        return "http://" + url

def AdminGrabber(url, wordlist):
	try:
##		url = urlFix(raw_input("Enter URL: "))
		ua = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"
		header = {'User-Agent' : ua}

		req = urllib2.Request(url, None, header)
		resp = urllib2.urlopen(req)

		print(sap)
		print("[Connecting] : %s..." % url)

		if resp.code == 200:
			time.sleep(2)
			print("[Connected]  : %s is connected" % url)
			print(sap)

	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")

	except:
		print(sap)
		print("[Connecting] : %s" % url)
		time.sleep(2)

		print("[Failed] : %s is offline or invalid URL" % url)
		print(sap)
		sys.exit()

        flag = 0
        panel = []
        wordlist = wordlist

	try:
                f_in = open(wordlist)
                panel = list(line for line in (l.strip() for l in f_in) if line)
		badlength = len(panel)
		print("[Loaded]  : %d Panels Loaded.." % badlength)
		time.sleep(2)
		panel = list(set(panel)) # this will remove duplicates [a set has no duplicates]
		length = len(panel)
		print("[Using]   :"),
		print("%d/%d Panels being used (%d duplicates).." % (length, badlength, badlength - length))

	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")

	except IOError as error:
		print("[Error]   : %s not found" % wordlist)
		print(sap)
		sys.exit()

	try:
		print(sap)
                

		if length > 0: # Checking validity of Wordlist
			time.sleep(2)
			print("\n[Checking] : Checking Admin Panels  ")
			print("---------------------------------------")
			print("| Resp     :        Results           |")
			print("---------------------------------------")
			counter = 1
			for x in panel:
				x = "/" + x
				payload = url + x
				string = '[%d] : %s' % (counter, payload)
				newline = len(string) * ' '
				sys.stdout.write("%s%s\r" % (string, newline))
				counter += 1
				try:
					#correction of duplication of http or https
					payload = payload.replace("//", "/")
					payload = payload.replace("http:/", "http://")
					payload = payload.replace("https:/", "https://")

					plreq = urllib2.Request(payload, headers=header)
					plresp = urllib2.urlopen(plreq)

				except KeyboardInterrupt:
					sys.exit("\n[User Interrupt] : Exiting .. ")

				except:
					pass
				else:
					if plresp.code == 200: #show pages with proper response
						flag = 1
						print "====================================================="
						print("  [OK]     :        %s" % payload)
						print "====================================================="
						
					elif plresp.code == 302: #show redirected pages
						flag = 1
						print "====================================================="
						print("  [FOUND]  :        %s" % payload)
						print "====================================================="

					elif plresp.code == 403: #show Forbbiden pages
						flag = 1
						print "====================================================="
						print("  [FORBBIDEN] :     %s" % payload)
						print "====================================================="

			if not flag:
				print("[NO PANEL] : No Panel Found.. ")

		else:
			print("[Error]    : Enter a valid wordlist ..")

	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")

def Main():
        print(banner)
        usage       = '''%prog [-h] [-v] [-u "url"] [-w 'wordlist.txt']'''
        version     = "%prog version 1.0"
        description = 'A cross-platform python based utility to find admin panels of websites.'
        parser = optparse.OptionParser(usage=usage,version=version,conflict_handler="resolve", description=description)
        general = optparse.OptionGroup(parser, 'General')
        general.add_option(
                '-h', '--help',
                action='help',
                help='Shows the help and exit.')
        general.add_option(
                '-v', '--version',
                action='version',
                help='Shows the version and exit.')
        target = optparse.OptionGroup(parser, "Target")
        target.add_option(
                "-u", "--url", 
                action='store_true',
                dest='web',\
                help="Target website to find admin panel.")
        target.add_option(
                "-w", "--wordlist", 
                action='store_true',
                dest='wordlist',\
                help="Specify wordlist of admin panel.")
        parser.add_option_group(general)
        parser.add_option_group(target)
        (options, args) = parser.parse_args()
        if not options.web and not options.wordlist:
                parser.print_help()
        elif options.web and options.wordlist:
                url = args[0]
                wordlist = args[1]
                AdminGrabber(url, wordlist)
        else:
                parser.print_help()
if __name__ == "__main__":
	Main()
