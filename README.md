Twitter Spam Detector
=====================
This project was born as a homegrown utility for spam detection on a `#vldc` Twitter hastag.

Spam detector is very simple Naive Bayes Multinomial Classifier. There are some additional
twitter related tools also.

Installation
============
Python *and* PHP are prerequirements and should be installed. It's a shame, but I provide this software
AS IS, sorry guys :) PHP required only for retweeting, so if you don't need retweeting functionality
you can skip this requirement.

What you should do, is to put your twitter name and password in `.pass` file. This step is
required because of Twitter Streaming API use basic HTTP authentication with user loging and password.
This could be easily done with following command:

	echo "login:secret" > .pass
	
Also you should put your consumer token, access token and their secrets in `.oauth.php` file in a
following format:

	<?php
	$conf = array(
		'consumer_key'    => 'AvExZTKfB1lMVuD8t4xUL',
		'consumer_secret' => 'yCmk6gZstEYq6mf1IwVDhQykdLjojyr7nFySDZG4',
		'user_token'      => '847135758-JTMuVBsdwzQT7jfx2CjLBg5twDGIf5Uwhg3Vcspa',
		'user_secret'     => 'jWI2BbKQWNVQj2JFJvYuDwFi7vuEQfhyzMZcVB6wvZ5',
	);
	
*NOTICE*: values provided here _are not_ valid Twitter OAuth keys and given for demonstration
purpose only

This keys could be generated while using [dev.twitter.com][ref-twitter-dev].

Run
===
No surprise here.

	./run

Content
=======
Sources contains several scripts for learning and classifiying probablistic bayes models as well as
streaming and retweeting tweets in realtime.

* `learn.py` — learn naive bayes classification model. This script require prepared dataset on input
(see `dataset` as a example). Using: `cat dataset | ./learn.py model.m`
* `classify.py` — classify tweets as a spam or not. Requires tweets in json format on input, one per line. 
* `stream-tweets` — shell script streaming tweets with hashtag `#vldc` on stdout in realtime. Used with `classify.py` to classify tweets.

[ref-twitter-dev]: https://dev.twitter.com/apps