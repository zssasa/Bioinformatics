# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint

def ReadScoreMatrix(file):
	scoreMatrix = dict()
	with open(file) as f:
		proteins = f.readline().strip().split()
		for line in f:
			line = line.strip().split()
			for i in range(len(proteins)):
				scoreMatrix[(line[0],proteins[i])] = int(line[i+1])
	return scoreMatrix
	# print(proteins)

def GlobalBackTrack(str1, str2, scoreMatrix, indel):
	S = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	BackTrack = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	for i in range(1,len(str1)+1):
		S[i][0] = S[i-1][0] - indel
	for j in range(1,len(str2)+1):
		S[0][j] = S[0][j-1] - indel
	for i in range(1,len(str1)+1):
		for j in range(1,len(str2)+1):
			S[i][j] = max(S[i-1][j] - indel,S[i][j-1] - indel,S[i-1][j-1] + scoreMatrix[(str1[i-1],str2[j-1])])
			if S[i][j] == S[i-1][j] - indel:
				BackTrack[i][j] = 2
			elif S[i][j] == S[i][j-1] - indel:
				BackTrack[i][j] = 3
			elif S[i][j] == S[i-1][j-1]+ scoreMatrix[(str1[i-1],str2[j-1])]:
				BackTrack[i][j] = 1
	return BackTrack, S[len(str1)][len(str2)]

def OutputGlobal(backtrack, str1, str2, i, j):
	#s = []
	s1 = ''
	s2 = ''
	while i>0 and j>0:
		if backtrack[i][j] == 1:
			s1 += str1[i-1]
			s2 += str2[j-1]
			#s.append(v[i-1])
			i -= 1
			j -= 1
		elif backtrack[i][j] == 2:
			s1 += str1[i-1]
			s2 += '-'
			i -= 1
		else:
			s1 += '-'
			s2 += str2[j-1]
			j -= 1
	while i>0:
		s1 += str1[i-1]
		s2 += '-'
		i -= 1
	while j>0:
		s1 += '-'
		s2 += str2[j-1]
		j -= 1
	return s1[::-1], s2[::-1]

def GlobalAlignment(str1, str2, scoreMatrix, indel):
	backtrack, score = GlobalBackTrack(str1, str2, scoreMatrix, indel)
	s1, s2 = OutputGlobal(backtrack,str1, str2, len(str1), len(str2))
	return s1, s2, score

if __name__ == '__main__':
	scoreMatrix = ReadScoreMatrix('PAM250.txt')
	# pprint(scoreMatrix)
	# str1 = 'PLEASANTLY'
	# str2 = 'MEANLY'
	# indel = 5
	# with open('./data/global_alignment_test.txt') as f:
	with open('local_train.txt') as f:

		str1 = f.readline().strip()
		str2 = f.readline().strip()
	indel = 5
	s1,s2,score = GlobalAlignment(str1, str2, scoreMatrix, indel)
	print(score)
	print(s1)
	print(s2)