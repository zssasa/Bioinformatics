# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from PatternCount import PatternCount

def FrequentWords(Text, k):
	FrequentPatterns = set()
	count  = [0] * (len(Text)-k+1)
	for i in range(len(Text)-k+1):
		pattern = Text[i:i+k]
		count[i] = PatternCount(Text, pattern)
	maxCount = max(count)
	for i in range(len(Text)-k+1):
		if count[i] == maxCount:
			FrequentPatterns.add(Text[i:i+k])
	return FrequentPatterns

