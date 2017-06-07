<?php 

function checkSubDomains($website) { 

	$combo = "http://www.pagesinventory.com/search/?s=" . $website;

	$get = file_get_contents($combo);

	$new = str_replace("<tr>", "\n<tr>", $get);

	preg_match_all("/" . base64_decode("PHRyIGNsYXNzPVwic3VkZVwiPjx0ZD48YSBocmVmPVwiKC4qKVwiPiguKik8XC9hPjxcL3RkPjx0ZCBjbGFzcz1cInRiLXJpZ2h0XCI+KC4qKTxcL3RkPjx0ZCBjbGFzcz1cInRiLXJpZ2h0XCI+KC4qKTxcL3RkPjx0ZCBjbGFzcz1cInRiLXJpZ2h0XCI+KC4qKTxcL3RkPjx0ZCBjbGFzcz1cInRiLXJpZ2h0XCI+PGEgaHJlZj1cIiguKilcIj4oLiopPFwvYT48XC90ZD48dGQgY2xhc3M9XCJ0Yi1yaWdodFwiPiguKik8XC90ZD48XC90cj4=") . "/i", $new, $matches);

	$subdomains = $matches[2];
	$ip = $matches[7];

	$total = count($matches[2]);

	if (!($total == "0")) {

		$tot = $total - 1;

		echo "\n[\$] Total SubDomains: " . $tot . "";
		echo "\n\n";

		for ($i = 0; $i < count($subdomains) && $i < count($ip); ++$i) {
		    $website = $subdomains[$i];
		    $info = $ip[$i];
		    echo " Domain: " .$website . " ==> ". $info."\n";

		    // took approx 1 hour to code :3 this script ^_^ with <3
		}
	} 

	else {
		die("[\$] Sorry There Aren't Any Sub Domains of The Website Your Entered.\n");
	}
}

?>