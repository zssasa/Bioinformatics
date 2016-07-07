# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

def OverlapGraph(lines):
	lines = sorted(lines)
	result = []
	for i in range(len(lines)):
		for j in range(len(lines)):
			if lines[i][1:] == lines[j][:-1]:
				result.append((lines[i],lines[j]))
	return result


