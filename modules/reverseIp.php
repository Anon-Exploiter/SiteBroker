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

function reverseIP($site){
	
	$red = "\033[1;31m";

	$url = 'http://domains.yougetsignal.com/domains.php';

	$data = 
	array(
		'remoteAddress' => $site
	);

	$options =
	array(
		'http' => array(
			'method' => 'POST',
			'request_fulluri' => true,
			'header' => 'Content-type: application/x-www-form-urlencoded',
			'content' => http_build_query($data)
		)
	);

	$context = stream_context_create($options);
	$result = file_get_contents($url, false, $context);

	if (preg_match_all('/\["(.*?)",/i', $result, $match)) {

		echo "\n";
		echo " [\$] IP = ".gethostbyname($site) ."\n";
		echo " [\$] Total Domains : ".count($match[1])."\n\n";

		foreach ($match[1] as $websites) {
			echo " ". $red ."".$websites."\n";
			//thanks to inj3ctor 0sman <3 
		}
	}
}


?>