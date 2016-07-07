# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from ComputingFrequencies import ComputingFrequencies
from ComputingFrequencies import PatternToNumber
from ComputingFrequencies import NumberToPattern

def ClumpFinding(Genome, k, t, L):
	FrequentPatterns = set()
	Clump = [0] * (4**k)
	Text = Genome[0:L]
	FrequencyArray = ComputingFrequencies(Text, k)
	# Clump[FrequencyArray>=t] = 1
	for i in range(4**k):
		if FrequencyArray[i] >= t:
			Clump[i] = 1
	for i in range(1,len(Genome)-L+1):
		FirstPattern = Genome[i-1:i+k-1]
		index = PatternToNumber(FirstPattern)
		FrequencyArray[index] -= 1
		LastPattern = Genome[i+L-k:i+L]
		index = PatternToNumber(LastPattern)
		FrequencyArray[index] += 1
		if FrequencyArray[index] >= t:
			Clump[index] = 1
	for i in range(4**k):
		if Clump[i] == 1:
			# print(i)
			pattern = NumberToPattern(i,k)
			FrequentPatterns.add(pattern)

	return FrequentPatterns

