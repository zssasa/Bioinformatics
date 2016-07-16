# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def PairedComposition(text, k, d):
	result = []
	for i in range(len(text)-2*k-d+1):
		result.append([text[i:i+k],text[i+k+d:i+2*k+d]])
	result = sorted(result)
	return result

if __name__ == '__main__':
	text = 'TAATGCCATGGGATGTT'
	k = 3
	d = 2
	s = PairedComposition(text,k,d)
	for pair in s:
		print('(%s|%s)' % (pair[0],pair[1]),end=' ')
