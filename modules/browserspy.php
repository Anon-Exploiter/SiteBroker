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

function browserSpy($website) {

	$url = 'http://browserspy.dk/webserver.php';

	$data = 
	array(
		'server' => $website
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
	$get = file_get_contents($url, false, $context);

	preg_match_all("/<tr class=\"(.*)\">\n<td class=\"property\">(.*)<\/td>\n<td class=\"value\">(.*)<\/td>\n<\/tr>/i", $get, $matches);

	$title = $matches[2];

	$content = $matches[3];

	echo "\n";

	for ($i = 0; $i < count($title) && $i < count($content); ++$i) {
	    $website = $title[$i];
	    $info = $content[$i];

	    echo " [\$] " . $website . " : " . $info . "\n";
	}

}


?>
