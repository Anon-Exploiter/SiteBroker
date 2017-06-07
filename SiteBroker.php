<?php

/*
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

                                ~ Changing Author Name Wont Make You One :) 
                                             #Respect Coders
*/

#############################################################################

include "internels/colors.php";
include "internels/banner.php";
include "internels/errors.php";
include "modules/functions.php";

#############################################################################

// Lets print the Banner

//execute("cd modules/;python clear.py");

echo $banner;

// Lets proceed to thy Script :)

echo $blue . "\n [\$] Please Enter The Website You Want To Scan " . $red . "(Dont Use http\\https\\www):" . $yellow . " ";

$argument = trim(fgets(STDIN, 1024));

if (!empty($argument)) {

	$website = checkWebsite($argument); // let me see what are you inputting :P

	echo $green . "\n [\$] What You Wanna Do With The Given Website ? \n\n 1). Cloudlfare Bypass. \n 2). Website Crawler.\n 3). Reverse IP.\n 4). Information Gathering.\n 5). Nameservers.\n 6). WebSite Speed.\n 7). Subdomains Scanner\n 8). Shell Finder.\n 9). All Things.\n 10). Admin Panel Finder.\n\n " . $cyan . "[\$] Select Any Of Thy Indexes (i.e, 1, 2, 3): ";

	$argument = trim(fgets(STDIN, 1024));
	
	if (is_numeric($argument)) { // Checking whether it is a numeric value or not
		
		if ($argument == "1") {

			echo $green . "\n [+] Started To See If The Website is Using Cloudlfare: \"" . $website . "\"\n\n" . $white . "";
			include "modules/ip.php";
			realIp($website);
			echo "\n [\$] Searching Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";
		}

		elseif ($argument == "2") {

			echo $green . "\n [+] Started To Crawl The Website For Parameters: \"" . $website . "\"\n" . $yellow . "";
			$command = "cd scripts/Crawler/;php crawler.php " . checkInputWebsite($website) . "";
			$result = execute($command);
			echo $result . "\n\n [\$] Crawling Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

		}

		elseif ($argument == "3") {
			
			echo $green . "\n [+] Started To Do Reverse IP Of \"" . $website . "\"\n" . $yellow . "";
			include "modules/reverseIp.php";
			reverseIP($website);
			echo "\n\n [\$] Reverse IP Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";
		}

		elseif ($argument == "4") {

			echo $green . "\n [\$] Starting To Do Information Gathering of \"" . $website . "\"\n";
			echo $blue . "\n [\$] What You Wanna Do With The Given Website ?\n\n";
			echo $green . " 1). Whois Lookup\n";
			echo $yellow . " 2). NetCraft Site Report\n";
			echo $cyan . " 3). BrowserSpy Report\n";
			echo $red . " 4). All Things\n\n";
			echo $yellow . " [\$] Select Any Of Thy Indexes (i.e, 1, 2, 3): ";

			// taking user's input
			$arg = trim(fgets(STDIN, 1024));

			// lets check whether it is numeric or not

			if (is_numeric($arg)) { // Okay so The Input is numeric lets proceed
				
				// checking the values of thy arguments

				if ($arg == "1") {

					// doing whois lookup in this block.
					
					echo $green . "\n [+] Started To Do Whois Lookup Of \"" . $website . "\"\n";
					echo $cyan;
					$command = "cd modules/;php whois.php " . $website . "";
					$result = execute($command);
					echo "\n" . $result. "\n";
					echo "\n [\$] Whois Lookup Done. ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

				}

				elseif ($arg == "2") {

					// generating netcraft report in this block.
					
					echo $green . "\n [+] Started To Generate NetCraft Report Of \"" . $website . "\"\n\n";
					echo $blue;
					include "modules/netcraft.php";
					echo websiteInfo($website);
					echo "\n [\$] NetCraft Report Generated. ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

				}

				elseif ($arg == "3") {

					// generating browserspy report in this block.
					
					echo $green . "\n [+] Started To Generate BrowserSpy Report Of \"" . $website . "\"\n";
					echo $cyan;
					include "modules/browserspy.php";
					echo browserSpy($website);
					echo "\n [\$] BrowserSpy Report Generated.\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

				}

				elseif ($arg == "4") {

					echo $green . "\n [+] Started To Find Every Index Given Above Of \"" . $website . "\"";
					echo $red."(#It May Take A While :)\n";

					//starting whois lookup here

					echo $green . "\n [+] Started To Do Whois Lookup Of \"" . $website . "\"\n";
					echo $cyan;
					$command = "cd modules/;php whois.php " . $website . "";
					$result = execute($command);
					echo "\n" . $result. "\n";
					echo "\n [\$] Whois Lookup Done. ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

					//generating netcraft report here

					echo $green . "\n [+] Started To Generate NetCraft Report Of \"" . $website . "\"\n";
					echo $blue;
					include "modules/netcraft.php";
					echo websiteInfo($website);
					echo "\n [\$] NetCraft Report Generated. ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

					// generating browserspy report.
					
					echo $green . "\n [+] Started To Generate BrowserSpy Report Of \"" . $website . "\"\n";
					echo $cyan;
					include "modules/browserspy.php";
					echo browserSpy($website);
					echo $green . "\n [\$] BrowserSpy Report Generated.\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

					// done :D
					
				}
			}

			else {
				die("\t".$val_error);
			}			
		}

		elseif ($argument == "5") {

			echo $green . "\n [+] Finding Nameservers Of \"" . $website . "\"\n" . $yellow . "";
			include "modules/nameservers.php";
			echo "\n".nameserver($website);
			echo "\n [\$] Finding Nameservers Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

		}

		elseif ($argument == "6") {

			echo $green . "\n [+] Started To Find Loading Speed Of \"" . $website . "\"".$red." (#It May Differ Somtimes)\n" . $yellow . "";
			$command = "cd scripts/SiteSpeedChecker/;python sitespeed.py -u " . checkInputWebsite($website) . "";
			$result = "\n" . execute($command);
			echo $result . "\n\n [\$] Finding Speed Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

		}

		elseif ($argument == "7") {

			echo $green . "\n [+] Started To Find Subdomains Of \"" . $website . "\"".$red."\n" . $yellow . "";
			include "modules/subdomains.php";
			echo "\n".checkSubDomains($website);
			echo "\n [\$] Finding Subdomains Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

		}

		elseif ($argument == "8") {

			echo $green . "\n [+] Finding Shells for \"" . $website . "\" " . $red . " (#ItMayTakeSomeTime)\n" . $yellow . "\n";
			include "modules/shell_finder.php";
			echo shellcheck(checkInputWebsite($website));
			echo $yellow . "\n [\$] Finding Shells Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

		}

		elseif ($argument == "9") {

			echo $green . "\n [+] Started To Find Every Index Given Above Of \"" . $website . "\"".$red." (#It May Take A While :)\n" . $yellow . "";

			// checking for cloudflare

			echo $green . "\n [+] Started To See If The Website is Using Cloudlfare: \"" . $website . "\"\n\n" . $white . "";
			include "modules/ip.php";
			realIp($website);
			echo "\n [\$] Searching Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

			// lets crawl the bitch :P 

			echo $green . "\n [+] Started To Crawl The Website For Parameters: \"" . $website . "\"\n" . $yellow . "";
			$command = "cd scripts/Crawler/;php crawler.php " . checkInputWebsite($website) . "";
			$result = execute($command);
			echo $result . "\n\n [\$] Crawling Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

			// lets do the reverse ip of the website

			echo $green . "\n [+] Started To Do Reverse IP Of \"" . $website . "\"\n" . $yellow . "";
			include "modules/reverseIp.php";
			echo reverseIP($website);
			echo "\n\n [\$] Reverse IP Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

			// Lets do information gathering of the website

					echo $green . "\n [+] Started To Find Every Index Given Above Of \"" . $website . "\"";
					echo $red."(#It May Take A While :)\n";

					//starting whois lookup here

					echo $green . "\n [+] Started To Do Whois Lookup Of \"" . $website . "\"\n";
					echo $cyan;
					$command = "cd modules/;php whois.php " . $website . "";
					$result = execute($command);
					echo "\n" . $result. "\n";
					echo "\n [\$] Whois Lookup Done. ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

					//generating netcraft report here

					echo $green . "\n [+] Started To Generate NetCraft Report Of \"" . $website . "\"\n";
					echo $blue;
					include "modules/netcraft.php";
					echo websiteInfo($website);
					echo "\n [\$] NetCraft Report Generated. ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

					// generating browserspy report.
					
					echo $green . "\n [+] Started To Generate BrowserSpy Report Of \"" . $website . "\"\n";
					echo $cyan;
					include "modules/browserspy.php";
					echo browserSpy($website);
					echo $green . "\n [\$] BrowserSpy Report Generated.\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

			// lets check the loading speed of the website


			echo $green . "\n [+] Started To Find Loading Speed Of \"" . $website . "\"".$red." (#It May Differ Somtimes)\n" . $yellow . "";
			$command = "cd scripts/SiteSpeedChecker/;python sitespeed.py -u " . checkInputWebsite($website) . "";
			$result = "\n" . execute($command);
			echo $result . "\n\n [\$] Finding Speed Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

			// lets check subdomains

			echo $green . "\n [+] Started To Find Subdomains Of \"" . $website . "\"".$red."\n" . $yellow . "";
			include "modules/subdomains.php";
			echo "\n".checkSubDomains($website);
			echo "\n [\$] Finding Subdomains Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

			//lets check for shells B)

			echo $green . "\n [+] Finding Shells for \"" . $website . "\" " . $red . " (#ItMayTakeSomeTime)\n" . $yellow . "\n";
			include "modules/shell_finder.php";
			echo shellcheck(checkInputWebsite($website));
			echo $yellow . "\n [\$] Finding Shells Done ^_^\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";

		}

		elseif ($argument == "10") {

			echo $green . "\n [+] Started To Find Admin Panel Of \"" . $website . "\" " . $red . "(#BePatient It Takes 5 to 10 minutes)\n" . $cyan . "";
			$command = "cd scripts/Admin_Panel_Founder/;python adgrab.py --url " . checkInputWebsite($website) . " --wordlist wordlist.txt";
			$result = execute($command);
			echo $result . "\n\n [\$] Admin Panel Found :)\n\tThanks For Using :D \n\t\t~ An0n 3xPloiTeR\n";
		}

		else {
			die($val_select);
		}

	} 

	elseif (!is_numeric($argument)) { // I think it isn't :/ 
		die($val_error);
	}
}

elseif (empty($argument)) {
	die($errno);
}

?>
