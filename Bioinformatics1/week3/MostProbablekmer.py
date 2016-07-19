# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def MostProbableKmer(text, k, profile):
	maxProb = 0
	index = 0
	for i in range(len(text)-k+1):
		prob = 1
		for j in range(k):
			if text[i+j] == 'A':
				prob *= profile[0][j]
			elif text[i+j] == 'C':
				prob *= profile[1][j]
			elif text[i+j] == 'G':
				prob *= profile[2][j]
			else:
				prob *= profile[3][j]
		if prob > maxProb:
			maxProb = prob
			index = i
	return text[index:index+k]



if __name__ == '__main__':
	with open('./data/MostProbablekmer_test.txt') as f:
		text = f.readline().strip()
		k = int(f.readline().strip())
		lines = f.readlines()
	profile = []
	for line in lines:
		profile.append(list(map(float,line.strip().split())))
	# text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
	# k = 5
	# profile= [[0.2, 0.2, 0.3, 0.2, 0.3],[0.4, 0.3, 0.1, 0.5, 0.1],
	# 		  [0.3, 0.3, 0.5, 0.2, 0.4],[0.1, 0.2, 0.1, 0.1, 0.2]]
	print(MostProbableKmer(text,k,profile))
