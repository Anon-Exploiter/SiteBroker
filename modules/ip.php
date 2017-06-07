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

function realIp($input) {

	$dns = dns_get_record($input, DNS_MX);

	$mx_record=$dns[0]['target'];

	$ip = gethostbyname($mx_record);

	$n = gethostbyaddr($ip);

	echo " [\$] This is the Real ip \"" . $ip . "\" of " . $input . " \n";
	
	echo " [\$] It is also referred to $n\n";

	// thanks to inj3ct0r 0sman <3

}

?>
