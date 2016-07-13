# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from HammingDistance import hamming_distance
from ApproximatePattern import approximate_pattern_count

Nucleotides = {'A','C','G','T'}
NucleotideToNumber = {'A':0, 'C':1, 'G':2, 'T':3}
NumberToNucleotide = ['A', 'C', 'G', 'T']
ReverseDict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}


def ReverseSequence(Sequence):
	result = ""
	for i in range(len(Sequence)-1,-1,-1):
		# print(i)
		result += ReverseDict[Sequence[i]]
	return result

def PatternToNumber(pattern):
	ll = len(pattern)
	result = 0
	for i in range(ll):
		# print('previous result is : %d' %result)
		# print('pattern i is %s' %pattern[i])
		# print('Nulceotide numbre is %d' %NucleotideToNumber[pattern[i]])
		result = 4*result + NucleotideToNumber[pattern[i]]
		# print('later result is : %d\n' %result)
	return result


def NumberToPattern(index, k):
	if k==1:
		return NumberToNucleotide[index]
	prefixIndex = index // 4
	r = index % 4
	symbol = NumberToNucleotide[r]
	prefixPattern = NumberToPattern(prefixIndex, k-1)
	return prefixPattern+symbol



def Neighbors(pattern, d):
	if d == 0:
		return {pattern}
	if len(pattern) == 1:
		return {'A','C','G','T'}
	Neighborhood = set()
	SufficeNeighbors = Neighbors(pattern[1:],d)
	for str in SufficeNeighbors:
		if hamming_distance(str,pattern[1:]) < d:
			for base in Nucleotides:
				# print(base)
				Neighborhood.add(base+str)
		else:
			Neighborhood.add(pattern[0]+str)
	return Neighborhood

def FrequentWordsWithMismatches(text, k, d):
	FrequentPatterns = set()
	close = [0] * (4**k)
	FrequencyArray = [0] * (4**k)
	for i in range(len(text)-k+1):
		neighbors = Neighbors(text[i:i+k],d)
		for pattern in neighbors:
			index = PatternToNumber(pattern)
			close[index] = 1
	for i in range(4**k):
		if close[i] == 1:
			pattern = NumberToPattern(i, k)
			FrequencyArray[i] = approximate_pattern_count(pattern, text, d)

	maxCount = max(FrequencyArray)
	for i in range(4**k):
		if FrequencyArray[i] == maxCount:
			pattern = NumberToPattern(i, k)
			FrequentPatterns.add(pattern)
	return FrequentPatterns

def FrequentWordsWithMismatchesSorted(text, k, d):
	FrequentPatterns = set()
	Neighborhoods = []
	for i in range(len(text)-k+1):
		Neighborhoods.extend(list(Neighbors(text[i:i+k],d)))
	# Neighborhoods = list(set(Neighborhoods))
	index = [0] * len(Neighborhoods)
	count = [0] * len(Neighborhoods)

	# print(Neighborhoods)
	for i in range(len(Neighborhoods)):
		pattern = Neighborhoods[i]
		index[i] = PatternToNumber(pattern)
		count[i] = 1
	# print(index)
	# print(count)
	sortedIndex = sorted(index)
	# print(sortedIndex)
	for i in range(len(Neighborhoods)-1):
		if sortedIndex[i] == sortedIndex[i+1]:
			count[i+1] = count[i] + 1
	maxCount = max(count)
	# print(maxCount)
	for i in range(len(count)):
		if count[i] == maxCount:
			pattern = NumberToPattern(sortedIndex[i], k)
			FrequentPatterns.add(pattern)
	return FrequentPatterns


def FrequentWordsWithMismatchesAndReverseComplements(text, k, d):
	FrequentPatterns = set()
	close = [0] * (4**k)
	FrequencyArray = [0] * (4**k)
	for i in range(len(text)-k+1):
		neighbors = Neighbors(text[i:i+k],d)
		# if ReverseSequence(text[i:i+k]) != text[i:i+k]:
		# 	neighbors = neighbors | Neighbors(ReverseSequence(text[i:i+k]),d)
		for pattern in neighbors:
			index = PatternToNumber(pattern)
			close[index] = 1
	for i in range(4**k):
		if close[i] == 1:
			pattern = NumberToPattern(i, k)
			FrequencyArray[i] = approximate_pattern_count(pattern, text, d)
			if pattern != ReverseSequence(pattern):
				FrequencyArray[i] += approximate_pattern_count(ReverseSequence(pattern), text, d)


	maxCount = max(FrequencyArray)
	for i in range(4**k):
		if FrequencyArray[i] == maxCount:
			pattern = NumberToPattern(i, k)
			FrequentPatterns.add(pattern)
	return FrequentPatterns


if __name__ == '__main__':
	# with open('./data/Neighbors_test.txt') as f:
	# 	pattern = f.readline().strip()
	# 	d = int(f.readline().strip())
	# pattern = 'ACG'
	# d = 1
	# neighbors = Neighbors(pattern,d)
	# for s in neighbors:
	# 	print(s)
	# text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
	# k = 4
	# d = 1
	# with open('./data/FrequentWordsWithMismatches_test.txt') as f:
	# 	text = f.readline().strip()
	# 	k, d = list(map(int,f.readline().split()))
	# 	print(s)
	# print(type(s))
	# FrequentPatterns = FrequentWordsWithMismatches(text, k, d)
	# for pattern in FrequentPatterns:
	# 	print(pattern, end=' ')
		# print(PatternToNumber(pattern))

	# s = FrequentWordsWithMismatchesSorted(text,k,d)
	# for ss in s:
	# 	print(ss)
	# 	print(PatternToNumber(ss))

	with open('./data/FrequentWordsWithMismatchesAndReverseComplements_test.txt') as f:
		text = f.readline().strip()
		k, d = list(map(int,f.readline().split()))
	FrequentPatterns = FrequentWordsWithMismatchesAndReverseComplements(text, k, d)
	for pattern in FrequentPatterns:
		print(pattern, end=' ')

	pattern = 'ACGT'
	d = 3
	print(Neighbors(pattern,d))
	print(len(Neighbors(pattern,d)))



