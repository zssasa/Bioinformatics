# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


NucleotideToNumber = {'A':0, 'C':1, 'G':2, 'T':3}
NumberToNucleotide = ['A', 'C', 'G', 'T']

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




def ComputingFrequencies(Text, k):
	FrequencyArray = [0] * (4**k)
	for i in range(len(Text)-k+1):
		pattern = Text[i:i+k]
		j = PatternToNumber(pattern)
		FrequencyArray[j] += 1
	return FrequencyArray