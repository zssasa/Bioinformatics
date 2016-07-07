# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

def GenomePathString(lines):
	lines = [line.strip() for line in lines]
	# print(len(lines))
	genome = lines[0]
	for i in range(1,len(lines)):
		genome += lines[i][-1]
	return genome
