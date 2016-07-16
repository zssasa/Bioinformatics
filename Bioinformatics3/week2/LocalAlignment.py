# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint
import numpy as np

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


def LocalBackTrack(str1, str2, scoreMatrix, indel):
	S = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	BackTrack = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	for i in range(1,len(str1)+1):
		S[i][0] = max(S[i-1][0] - indel,0)
	for j in range(1,len(str2)+1):
		S[0][j] = max(S[0][j-1] - indel,0)
	for i in range(1,len(str1)+1):
		for j in range(1,len(str2)+1):
			S[i][j] = max(0, S[i-1][j] - indel,S[i][j-1] - indel,S[i-1][j-1] + scoreMatrix[(str1[i-1],str2[j-1])])
			if S[i][j] == 0:
				BackTrack[i][j] = 4
			elif S[i][j] == S[i-1][j] - indel:
				BackTrack[i][j] = 2
			elif S[i][j] == S[i][j-1] - indel:
				BackTrack[i][j] = 3
			elif S[i][j] == S[i-1][j-1]+ scoreMatrix[(str1[i-1],str2[j-1])]:
				BackTrack[i][j] = 1
			# elif S[i][j] == 0:
			# 	BackTrack[i][j] = 4
	# pprint(S)
	# print(max(max(S)))
	# pprint(BackTrack)
	S = np.array(S)
	# print(S.shape)
	# pprint(S[81][65:70])
	# pprint(S[82][65:70])
	# pprint(S[83][65:70])
	# pprint(S[84][65:70])
	# pprint(S[85][65:70])
	# t = np.array(BackTrack)
	# pprint(t[81][65:70])
	# pprint(t[82][65:70])
	# pprint(t[83][65:70])
	# pprint(t[84][65:70])
	# pprint(t[85][65:70])
	# pprint(t[86][65:70])
	# pprint(S[81:90][65:67])

	score = S.max()
	row, col = np.where(S==score)
	row = int(row)
	col = int(col)
	# print(row)
	# print(col)
	return BackTrack, S, row, col

def OutputLocal(backtrack, str1, str2, i, j):
	#s = []
	s1 = ''
	s2 = ''
	# while i>0 and j>0 and S[i][j]>0:
	while i>0 and j>0:
		# print('%d %d %d %d %s %s' %(i,j,S[i][j],backtrack[i][j],str1[i-1],str2[j-1]))
		# if S[i][j] == 0:
		# 	break
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
		elif backtrack[i][j] == 3:
			s1 += '-'
			s2 += str2[j-1]
			j -= 1
		else:
			break
	# print(i)
	# print(j)
	return s1[::-1], s2[::-1]

def LocalAlignment(str1, str2, scoreMatrix, indel):
	backtrack, score, row, col= LocalBackTrack(str1, str2, scoreMatrix, indel)
	s1, s2 = OutputLocal(backtrack, str1, str2, row, col)
	# pprint(backtrack[81:87][65:71])
	return s1, s2, score[row][col]

if __name__ == '__main__':
	scoreMatrix = ReadScoreMatrix('PAM250.txt')
	# pprint(scoreMatrix)
	# str1 = 'MEANLY'
	# str2 = 'PENALTY'
	# indel = 5
	with open('./data/local_alignment_train.txt') as f:
	# with open('local_train.txt') as f:

		str1 = f.readline().strip()
		str2 = f.readline().strip()
	indel = 5
	s1,s2,score = LocalAlignment(str1, str2, scoreMatrix, indel)
	print(score)
	print(s1)
	print(s2)
