#!/usr/bin/env python -u
import sys, json, math
from commons import *

def main():
	model = readModel(sys.argv[1])	
	
	while 1:
		line = sys.stdin.readline()
		if not line: break
		line = line.strip()
		if (len(line1) > 0):
			attr = json.loads(line)
			marker = "SPAM" if classify(model, attr) == "B" else "OK"
			text = attr['text'].encode('utf-8')
			print "{0:<5} {1[user][screen_name]:<20} {1[id]:<20} {2}".format(marker, attr, text)

main()