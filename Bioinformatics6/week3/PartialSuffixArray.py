# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def PartialSuffixArray(text,k):
	suffix = dict()
	partial_suffix = dict()
	for i in range(len(text)):
		suffix[text[i:]+text[:i]] = i
	sorted_suffix = sorted(suffix.items(),key=lambda x:x[0])
	for i in range(len(sorted_suffix)):
		if sorted_suffix[i][1]%k ==0 :
			partial_suffix[i] = sorted_suffix[i][1]
	return partial_suffix


if __name__ == '__main__':
	with open('./data/PartialSuffix_test.txt') as f:
		text =f.readline().strip()
		k = int(f.readline().strip())
	# text = 'PANAMABANANAS$'
	# k = 5
	s = PartialSuffixArray(text,k)
	for key in sorted(s.keys()):
		print('%d,%d' %(key,s[key]))