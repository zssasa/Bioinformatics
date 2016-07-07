# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def PatternMatch(pattern, Genome):
	result = []
	for i in range(len(Genome)-len(pattern)+1):
		if Genome[i:i+len(pattern)] == pattern:
			result.append(i)
	return result