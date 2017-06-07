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

       // It Took Me Too much time to code it. I hope you wont dissapoint me by changing names :)
                                			#An0n 3xPloiTeR

function websiteInfo($website) {

$url = "http://toolbar.netcraft.com/site_report?url=".$website;

$get = file_get_contents($url);

// Finding Title Here

echo "\n[\$] Grabbing Basic Information Of \"" . $website . "\" [\$]\n";

##################################################################################

$combination = "http://" . $website;

$get_site = file_get_contents($combination);

$title = "/<title>(.*)<\/title>/i";

preg_match($title, $get_site, $result);

echo "\n[\$] Site Title: ".$result[1]."\n";

##################################################################################

// Finding Date Here

$date = 
"/<th width=\"13%\">Date first seen<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($date, $get, $date_result);

echo "[\$] Date First Seen: ".$date_result[1]."\n";

// Finding Site Rank Here

$rank = 
"/<th width=\"13%\">Site rank<\/th>
<td width=\"37%\">


<a href=\"(.*)\">(.*)<\/a>
<\/td>/i";

preg_match($rank, $get, $rank_results);

echo "[\$] Site Rank: ".$rank_results[2]."\n";

// finding site's language here

$language = 
"/<th width=\"13%\">Primary language<\/th>
<td width=\"37%\">(.*)

<\/td>/i";

preg_match($language, $get, $language_results);

echo "[\$] Primary Language: ".$language_results[1]."\n";

//finding site's description of meta tag in here

$description = 
"/<th>Description<\/th>
<td colspan=\"3\">(.*)<\/td>/i";

preg_match($description, $get, $description_results);

echo "[\$] Description: ".$description_results[1]."\n";

echo "\n[\$] Grabbing Network Information [\$]\n\n";

$site = 
"/<th width=\"13%\">Site<\/th>
<td width=\"37%\"><a href='(.*)' target='_blank' rel='nofollow noreferrer'>(.*)<\/a><\/td>/i";

preg_match($site, $get, $site_results);

echo "[+] Site-Url: ".$site_results[2]."\n";

$netblock_owner =
"/<th width=\"13%\">Netblock Owner<\/th>
<td width=\"37%\"><a href='(.*)'>(.*)<\/a><\/td>/i";

preg_match($netblock_owner, $get, $netblock_owner_results);

echo "[+] Netblock-Owner: ".$netblock_owner_results[2]."\n";

$domain = 
"/<th width=\"13%\">Domain<\/th>
<td width=\"37%\"><a href='(.*)'>(.*)<\/a><\/td>/i";

preg_match($domain, $get, $domain_results);

echo "[+] Domain: ".$domain_results[2]."\n";

$nameserver =
"/<th width=\"13%\">Nameserver<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($nameserver, $get, $nameserver_results);

echo "[+] Nameserver: ".$nameserver_results[1]."\n";

$ip_address = 
"/<th width=\"13%\">IP address<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($ip_address, $get, $ip_results);

echo "[+] Ip Address: ".$ip_results[1]."\n";

$dns_admin = 
"/<th width=\"13%\">DNS admin<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($dns_admin, $get, $dns_results);

echo "[+] DNS Admin: ".$dns_results[1]."\n";

$ipv6 = 
"/<th width=\"13%\">IPv6 address<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($ipv6, $get, $ipv6_results);

echo "[+] IPv6 Results: ".$ipv6_results[1]."\n";

$reverse_dns = 
"/<th width=\"13%\">Reverse DNS<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($reverse_dns, $get, $reverse_dns_results);

echo "[+] Reverse DNS: ".$reverse_dns_results[1]."\n";

$domain_registrar = 
"/<th width=\"13%\">Domain registrar<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($domain_registrar, $get, $domain_registrar_results);

echo "[+] Domain Registrar: ".$domain_registrar_results[1]."\n";

$nameserver_organization =
"/<th width=\"13%\">Nameserver organisation<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($nameserver_organization, $get, $nameserver_org_results);

echo "[+] Nameserver Organization: ".$nameserver_org_results[1]."\n";

$organization = 
"/<th width=\"13%\">Organisation<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($organization, $get, $organization_results);

echo "[+] Organisation: ".$organization_results[1]."\n";

$hosting_company =
"/<th width=\"13%\">Hosting company<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($hosting_company, $get, $hosting_company_res);

echo "[+] Hosting Company: ".$hosting_company_res[1]."\n";

$level_domain = 
"/<th width=\"13%\">Top Level Domain<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($level_domain, $get, $level_domain_res);

echo "[+] Top Level Domain: ".$level_domain_res[1]."\n";

$dns_security = 
"/<th width=\"13%\">DNS Security Extensions<\/th>
<td width=\"37%\">(.*)<\/td>/i";

preg_match($dns_security, $get, $dns_security_res);

echo "[+] Dns Security Extensions: ".$dns_security_res[1]."\n";

$hosting_countr = 
"/<th width=\"13%\">Hosting country<\/th>
<td width=\"37%\"><a href='(.*)' target='_blank'><img src='(.*)' border='(.*)'\/>(.*)<\/a><\/td>/i";

preg_match($hosting_countr, $get, $hosting_coun);

if (strchr($hosting_coun[4], "&nbsp;")) {
	$hosting_co = str_replace("&nbsp;", "", $hosting_coun[4]);
} else {
	$hosting_co = $hosting_coun[4];
}

// hosting details goes here

echo "\n[\$] Grabbing Hosting Information\n\n";


echo "Hosting Country: ".$hosting_co."\n";


$hosting_details = 
"/<a href=\"(.*)\">(.*)<\/a>
<\/td>
                    <td>(.*)<\/td>
                    <td>(.*)<\/td>
                    <td>(.*)<\/td>
                    <td>(.*)<\/td>
                <\/tr>/i";

preg_match($hosting_details, $get, $hosting_details_res);

echo "[\$] Netblock owner: ".$hosting_details_res[2]."\n";

echo "[\$] IP Address: ".$hosting_details_res[3]."\n";

echo "[\$] OS: ".$hosting_details_res[4]."\n";

echo "[\$] Web server: ".$hosting_details_res[5]."\n";

echo "[\$] Last seen: ".$hosting_details_res[6]."\n";

echo "\n[\$] Extracting Website Information\n\n";

	if (file_exists("functions.php")) {

		include "functions.php";

		pregMatchForHTML($website);

		pregMatchForCSS($website);

		pregMatchForJS($website);

	}

preg_match_all("/" . base64_decode("PHRyIGNsYXNzPVwiKC4qKVwiPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRkIGNsYXNzPVwidGVjaG5vbG9neV9sYWJlbFwiPiguKilcczxhIGhyZWY9XCIoLiopXCIgcmVsPVwiKC4qKVwiIHRhcmdldD1cIiguKilcIiB0aXRsZT1cIiguKilcIj48aW1nIHNyYz1cIiguKilcIiBhbHQ9XCIoLiopXCJcLz48XC9hPjxcL3RkPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRkIGNsYXNzPVwidGVjaG5vbG9neV92YWx1ZVwiIHN0eWxlPVwid2lkdGg6NTAlXCI+KC4qKTxcL3RkPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHRkIGNsYXNzPVwiXCIgd2lkdGg9XCIzMCVcIj4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKPGEgaHJlZj1cIiguKilcIj4oLiopPFwvYT4sICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8YSBocmVmPVwiKC4qKVwiPiguKik8XC9hPiwgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCjxhIGhyZWY9XCIoLiopXCI+KC4qKTxcL2E+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8XC90ZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPFwvdHI+") . "/i", $get, $matches);

$lol = $matches[2];
$asdf = $matches[6];

echo "\n";

	for ($i = 0; $i < count($lol) && $i < count($asdf); ++$i) {
	    $website = $lol[$i];
	    $info = $asdf[$i];

	    echo "[\$] " . $website . " : ". $info."\n\n";
	}



}

?>