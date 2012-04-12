# -*- coding: utf8 -*-
import json, math

def normalize(text):
	return text.lower().replace("\n", " ")

def tokenize(text):
	return filter(lambda i: len(i) > 0, normalize(text).split(' '))

# строим по тексту набор feature по которым будет производится классификация
def getFeatures(js):
	text = js['text']
	words = tokenize(text)
	return words + [
		"___wordsCount:" + str(len(words)),
		"___linksCount:" + str(text.count("http://")),
		"___mentionCount:" + str(text.count("@")),
		"___hashCount:" + str(text.count("#")),
		"___source:" + js['source'],
		"___isRt:" + ("1" if 'rt' in words else "0")
	]

def readModel(fileName):
	fp = open(fileName, 'r')
	datum = []
	for x in range(4):
		datum.append(json.loads(fp.readline().strip()))
	fp.close()
	return datum
	
def writeModel(fileName, docCount, wordSize, wordProb, D):
	fp = open(fileName, 'w')
	fp.write(json.dumps(docCount) + "\n")
	fp.write(json.dumps(wordSize) + "\n")
	fp.write(json.dumps(wordProb) + "\n")
	fp.write(json.dumps(list(D)) + "\n")
	fp.close()

# производим классификацию и возвращаем наиболее подходящий класс для документа (спам/не спам)
def classify(model, js):
	(docCount, wordSize, wordProb, D) = model
	Gp = Bp = 0;
	for w in getFeatures(js):
		Gp += math.log(conditionalProbability(model, w, 'G'), 2)
		Bp += math.log(conditionalProbability(model, w, 'B'), 2)
	Gp += math.log(float(docCount['G']) / sum(docCount))
	Bp += math.log(float(docCount['B']) / sum(docCount))

	return "G" if Gp > Bp else "B"

def sum(dict):
	return reduce(lambda x, y: x + y, dict.values())
	
# расчитываем условную вероятность заданной feature для заданного класса
def conditionalProbability(model, word, klass):
	(docCount, wordSize, wordProb, D) = model
	return float(wordProb[klass].get(word, 0) + 1) / (sum(wordProb[klass]) + len(D))
