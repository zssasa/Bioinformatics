# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from HammingDistance import hamming_distance

NumberToNucleotide = ['A', 'C', 'G', 'T']



def DistanceBetweenPatternAndStrings(pattern, text):
	k = len(pattern)
	# print(k)
	dist = 0
	for str in text:
		HammingDistance = float("inf")
		for i in range(len(str)-k+1):
			if hamming_distance(pattern,str[i:i+k]) < HammingDistance:
				HammingDistance = hamming_distance(pattern,str[i:i+k])
		dist += HammingDistance
	return dist

def NumberToPattern(index, k):
	if k==1:
		return NumberToNucleotide[index]
	prefixIndex = index // 4
	r = index % 4
	symbol = NumberToNucleotide[r]
	prefixPattern = NumberToPattern(prefixIndex, k-1)
	return prefixPattern+symbol

def MedianString(text, k):
	dist = float("inf")
	# allMedian = dict()
	for i in range(4**k):
		pattern = NumberToPattern(i, k)
		if dist > DistanceBetweenPatternAndStrings(pattern,text):
			dist = DistanceBetweenPatternAndStrings(pattern,text)
			Median = pattern
	# for i in range(4**k):

	return Median

def AllMedian(text, k):
	dist = float("inf")
	allMedian = dict()
	for i in range(4**k):
		pattern = NumberToPattern(i, k)
		allMedian[pattern] = DistanceBetweenPatternAndStrings(pattern,text)
	minDist = min(list(allMedian.values()))
	result = [u for u,v in allMedian.items() if v==minDist]
	return result



if __name__ == '__main__':
	# with open('./data/DistanceBetweenPatternAndStrings_test.txt') as f:
	# 	pattern = f.readline().strip()
	# 	texts = f.readline().split()
	# texts = [text.strip() for text in texts]
	# print(pattern)
	# print(texts)
	# with open('./data/MedianString_test.txt') as f:
	# 	k = int(f.readline().strip())
	# 	texts = f.readlines()
	# texts = [text.strip() for text in texts]
	# k = 3
	# texts = ['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG','AGTTCGGGACAG']
	k = 7
	texts = ['CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC',
			 'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC',
			 'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG']


	# pattern = 'AAA'
	# text = ['TTACCTTAAC','GATATCTGTC','ACGGCGTTCG','CCCTAAAGAG','CGTCAGAGGT']
	# print(DistanceBetweenPatternAndStrings(pattern,texts))
	# print(MedianString(texts,k))
	print(AllMedian(texts,k))
