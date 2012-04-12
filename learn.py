#!/usr/bin/env python
import json, sys
from collections import defaultdict
from commons import *

def main():
	modelFileName = sys.argv[1]
	
	D = set()
	wordProb = {'B':defaultdict(int), 'G': defaultdict(int)}
	wordSize = {'B': 0, 'G': 0}
	docCount = {'B': 0, 'G': 0}

	for line in sys.stdin.readlines():
		parts = line.strip().split("\t")
		klass = parts[0]
		attr = json.loads(parts[1])
		docCount[klass] += 1
		for w in getFeatures(attr):
			D.add(w)
			wordProb[klass][w] += 1
			wordSize[klass] += 1
	
	writeModel(modelFileName, docCount, wordSize, wordProb, D)

main()