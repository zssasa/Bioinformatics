# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def skew(seq):
	s = [0] * (len(seq)+1)
	for i in range(len(seq)):
		if seq[i] == 'G':
			s[i+1] = s[i] + 1
		elif seq[i] == 'C':
			s[i+1] = s[i] - 1
		else:
			s[i+1] = s[i]
	return s

def minSkew(seq):
	s = skew(seq)
	t = min(s)
	index  = [i for i,v in enumerate(s) if v==t]
	# index = s.index(min(s[1:]))
	return index


if __name__ == '__main__':
	# with open('./data/skew_test.txt') as f:
	# 	seq = f.readline().strip()
	seq = 'CATTCCAGTACTTCGATGATGGCGTGAAGA'
	print(minSkew(seq))
