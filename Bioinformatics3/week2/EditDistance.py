# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint

def EditDistance(str1, str2):
	S = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	for i in range(1,len(str1)+1):
		S[i][0] = S[i-1][0]+1
	for j in range(1,len(str2)+1):
		S[0][j] = S[0][j-1]+1
	for i in range(1,len(str1)+1):
		for j in range(1,len(str2)+1):
			if str1[i-1] == str2[j-1]:
				cost = 0
			else:
				cost = 1
			S[i][j] = min(S[i-1][j]+1,S[i][j-1]+1,S[i-1][j-1]+cost)
	# pprint(S)
	return S[len(str1)][len(str2)]


if __name__ == '__main__':
	with open('./data/EditDistance_test.txt') as f:
		str1 = f.readline().strip()
		str2 = f.readline().strip()
	# str1 = 'PLEASANTLY'
	# str2 = 'MEANLY'
	print(EditDistance(str1,str2))
