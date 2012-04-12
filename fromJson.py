#!/usr/bin/env python
import json, sys, pprint, urllib

def check(t):
	return (t if t is not None else "").replace("\n", " ").encode("utf-8")
	
def main():
	for line in sys.stdin.readlines():
		js = json.loads(line)
		js['source'] = 
		datum = [js['source'], js['text']]
		print "\t".join(map(check, datum))

main()