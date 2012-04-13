<?php
require 'tmhOAuth.php';
require '.oauth.php';

$tmhOAuth = new tmhOAuth($conf);

$fp = fopen("php://stdin", "r");
while ($line = fgets($fp)) {
	$id = trim($line);
	$code = $tmhOAuth->request('POST', $tmhOAuth->url("1/statuses/retweet/{$id}"));
	if ($code == 200) {
		echo "Retweeting {$id}\n";
	}else{
		echo "Failed to retweet {$id}. Http status code: {$code}\n";
	}
}
fclose($fp);