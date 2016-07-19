# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

# from ../week2 import FrequentWordsWithMismatches
from FrequentWordsWithMismatches import  Neighbors
from HammingDistance import hamming_distance
def MotifEnumeration(texts, k, d):
	patterns = set()
	for j in range(len(texts[0])-k+1):
		pattern = texts[0][j:j+k]
		patterns |= Neighbors(pattern,d)
	for text in texts[1:]:
		neighbors = set()
		for i in range(len(text)-k+1):
			neighbor = Neighbors(text[i:i+k],d)
			neighbors |= neighbor
		patterns &= neighbors
	return patterns

	# # print(texts[0])
	# # patterns_mis = Neighbors(texts[0],d)
	# # print(patterns_mis)
	# for j in range(len(texts[0])-k+1):
	# 	pattern = texts[0][j:j+k]
	# 	neighbor = Neighbors(pattern,d)
	# 	print(neighbor)
	# 	for pattern_mis in neighbor:
	# 		flag = 0
	# 		for text in texts[1:]:
	# 			flag = 0
	# 			for i in range(len(text)-k+1):
	# 				if hamming_distance(pattern_mis,text[i:i+k]) < d:
	# 					flag = 1
	# 					break
	# 			if flag == 0:
	# 				break
	# 		if flag == 0:
	# 			break
	# 		else:
	# 			patterns.append(pattern_mis)
	# patterns = set(patterns)
	# return patterns


if __name__ == '__main__':
	with open('./data/MotifEnumeration_test.txt') as f:
		k, d = list(map(int,f.readline().strip().split()))
		texts = f.readlines()
	texts = [text.strip() for text in texts]
	# print(k)
	# print(d)
	# print(texts)
	s = MotifEnumeration(texts,k,d)
	for ss in s:
		print(ss,end=' ')



