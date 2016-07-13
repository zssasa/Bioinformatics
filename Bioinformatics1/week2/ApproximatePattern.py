# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from HammingDistance import hamming_distance

def approximate_pattern(pattern, text ,n):
	result = []
	for i in range(len(text)-len(pattern)+1):
		if hamming_distance(pattern,text[i:i+len(pattern)]) <= n:
			result.append(i)
	return result

def approximate_pattern_count(pattern, text, n):
	s = approximate_pattern(pattern,text,n)
	return len(s)

if __name__ == '__main__':
	# with open('./data/ApproximatePatternCount_test.txt') as f:
	# 	pattern = f.readline().strip()
	# 	text = f.readline().strip()
	# 	n = int(f.readline().strip())
	pattern = 'TGT'
	text = 'CGTGACAGTGTATGGGCATCTTT'
	n = 1
	# s = approximate_pattern(pattern,text,n)
	# print(len(s))
	# for ss in s:
	# 	print(ss,end=' ')
	print(approximate_pattern_count(pattern,text,n))

