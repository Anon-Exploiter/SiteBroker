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

// Lets Check The Website And Filter It.

function checkWebsite($input) {

	if (strchr($input, "https://")) {
		die("\t{=} Please Dont Use \"https://\" In Url :/\n\t\t~ An0n 3xPloiTeR\n");
	} 

	elseif (strchr($input, "http://")) {
		die("\t{=} Please Dont Use \"http://\" In Url :/\n\t\t~ An0n 3xPloiTeR\n");
	} 

	elseif (strchr($input, "www")) {
		die("\t{=} Please Dont Use \"www\" In Url :/\n\t\t~ An0n 3xPloiTeR\n");
	} 

	else {
		$website = $input;
	}

	return $website;

}

// included in netcraft.php

function pregMatchForHTML($website) {

    $get = file_get_contents("http://" . $website);

    echo "[\$] Checking If The Website Is Using \"HTML\"\n";

    if (preg_match('/<!doctype\shtml>/i', $get, $result, PREG_OFFSET_CAPTURE)) {

        echo "|\n";
        echo "|=====> It Is Using HTML\n";
        echo "|==========> Version Of HTML: It is using HTML5\n";

    }

    elseif (!preg_match('/<!doctype\shtml>/i', $get, $result, PREG_OFFSET_CAPTURE)) {

        echo "[\$] HTML: It is using HTML\n";
        echo "\t[-+-] Version Of HTML: It is using HTML < HTML5\n";

     }

}

// included for CSS in netcraft.php

function pregMatchForCSS($website) {

    $get = file_get_contents("http://" . $website);

    if (preg_match('/css/i', $get, $result, PREG_OFFSET_CAPTURE)) {

        echo "[\$] CSS: It is using CSS\n";
    }

    else {

        echo "[\$] CSS: Not Using CSS\n";

    }

}

// function for checking of JS. Included in netcraft.php

function pregMatchForJS($website) {

    $get = file_get_contents("http://" . $website);

    if (preg_match('/js/i', $get, $result, PREG_OFFSET_CAPTURE)) {

        echo "[\$] JavaScript: It is using JavaScript\n";

    } 

    elseif (preg_match('/javascript/i', $get, $result, PREG_OFFSET_CAPTURE)) {

        echo "[\$] JavaScript: It is using JavaScript\n";
        
    }

    else {

        echo "[\$] JavaScript: Not Using JavaScript\n";

    }

}

// Lets Use This Function If Some Commands Are Prohibited in The OS.

function execute($in) {

    $out = "";

    if (function_exists('exec')) {
        exec($in,$out);
        $out = join("\n",$out);
    } 

    elseif (function_exists('passthru')) {
        ob_start();
        passthru($in);
        $out = ob_get_clean();
    } 

    elseif (function_exists('system')) {
        ob_start();
        system($in);
        $out = ob_get_clean();
    } 

    elseif (function_exists('shell_exec')) {
        $out = shell_exec($in);
    } 

    elseif (is_resource($f = popen($in,"r"))) {
        $out = "";
        while(!feof($f))
            $out .= fread($f,1024);
        pclose($f);
    }

    return $out;

}

// Simple function for Checking websites

function checkInputWebsite($input) {

	if (!(strchr($input, "http://"))) {
		$website = "http://" . $input;
	}

	else {
		$website = $input;
	}

	return $website;

}

// Simple function for checking for reverse ip 

function checkWebsiteForReverseIp($input) {

	if (!(strchr($input, "http://"))) {
		$website = "http://www." . $input;
	}

	else {
		$website = $input;
	}

	return $website;

}


?>
