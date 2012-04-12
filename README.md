Twitter Spam Detector
=====================
This project was born as a homegrown utility for spam detection on a `#vldc` Twitter hastag.

Spam detector is very simple Naive Bayes Multinomial Classifier. There are some additional
twitter related tools also.

Content
=======
Sources contains several scripts for learning and classifiying probablistic bayes models as well as
streaming and retweeting tweets in realtime.

* `learn.py` — learn naive bayes classification model. This script require prepared dataset on input
(see `dataset` as a example). Using: `cat dataset | ./learn.py model.m`
* `classify.py` — classify tweets as a spam or not. Requires tweets in json format on input, one per line. 
* `stream-tweets` — shell script streaming tweets with hashtag `#vldc` on stdout in realtime. Used with `classify.py` to classify tweets.

Installation
============
What you should do, is to put your twitter name and password in `.pass` file. This step is
required because of Twitter Streaming API use basic HTTP authentication with user loging and password.
This could be easily done with following command:

	echo "login:secret" > .pass