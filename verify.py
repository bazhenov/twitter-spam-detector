#!/usr/bin/env python
import sys, json
from commons import *
	
def main():
	model = readModel(sys.argv[1])
	for line in sys.stdin.readlines():
		[klass, js] = line.strip().split("\t")
		attr = json.loads(js)
		print (classify(model, attr) + "\t" + klass + "\t" + normalize(attr['text'])).encode("utf-8")
	
main()