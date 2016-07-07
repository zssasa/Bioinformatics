# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def PatternCount(Text, pattern):
	count = 0
	for i in range(len(Text)-len(pattern)+1):
		if Text[i:i+len(pattern)] == pattern:
			count += 1
	return count
