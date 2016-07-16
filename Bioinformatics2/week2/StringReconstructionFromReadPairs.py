# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from EulerianPath import EulerianPath

def StringSpelledByPatterns(patterns, k):
	str = patterns[0]
	for i in range(1,len(patterns)):
		str += patterns[i][-1]
	return str

def StringSpelledByGappedPatterns(patterns, k, d):
	FirstPatterns = [u for u,v in patterns]
	SecondPatterns = [v for u,v in patterns]
	PrefixString = StringSpelledByPatterns(FirstPatterns, k)
	SuffixString = StringSpelledByPatterns(SecondPatterns, k)
	for i in range((k+d+1),len(PrefixString)):
		if PrefixString[i] != SuffixString[i-k-d]:
			return "there is no string spelled by the gapped patterns"
	return PrefixString+SuffixString[-k-d:]



def PairedDeBruijnGraph(patterns):
	result = dict()
	for pattern in patterns:
		PrefixPattern = (pattern[0][:-1],pattern[1][:-1])
		SuffixPattern = (pattern[0][1:],pattern[1][1:])
		if PrefixPattern in result:
			result[PrefixPattern].append(SuffixPattern)
		else:
			result[PrefixPattern] = [SuffixPattern]
	return result




if __name__ == '__main__':
	# with open('./data/StringReconstructionFromReadPairs_test.txt') as f:
	# 	k,d = list(map(int,f.readline().strip().split()))
	# 	patterns = f.readlines()
	# patterns = [list(pattern.strip().split('|')) for pattern in patterns]

	patterns = []
	with open('./data/probelmset3.txt') as f:
		for line in f:
			pattern = line.strip().split('|')
			patterns.append([pattern[0][1:],pattern[1][:-1]])
	print(patterns)
	k=3
	d=1

	# print(k)
	# print(d)
	# print(patterns)
	# print(StringSpelledByGappedPatterns(patterns,k,d))
	graph = PairedDeBruijnGraph(patterns)
	path = EulerianPath(graph)
	# print(path)
	# sortPatterns =
	s = StringSpelledByGappedPatterns(path,k,d)
	print(s)