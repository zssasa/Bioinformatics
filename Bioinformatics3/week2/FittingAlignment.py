# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint


def FittingAlignment(str1, str2, match_cost, mismatch_cost, indel):
	S = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	BackTrack = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]

	for i in range(1,len(str1)+1):
		S[i][0] = max(S[i-1][0]-1,0)
	for j in range(1,len(str2)+1):
		S[0][j] = S[0][j-1]-indel
	for i in range(1,len(str1)+1):
		for j in range(1,len(str2)+1):
			if str1[i-1] == str2[j-1]:
				cost = match_cost
			else:
				cost = mismatch_cost
			S[i][j] = max(S[i-1][j]-indel,S[i][j-1]-indel,S[i-1][j-1]+cost)
			if S[i][j] == S[i-1][j]-indel:
				BackTrack[i][j] = 2
			elif S[i][j] == S[i][j-1]-indel:
				BackTrack[i][j] = 3
			elif S[i][j] == S[i-1][j-1]+cost:
				BackTrack[i][j] = 1
	# pprint(S)
	# pprint(BackTrack)
	col = [s[-1] for s in S]
	row = col.index(max(col))
	return BackTrack,S[row][len(str2)],row,len(str2)

def OutputFitting(backtrack, str1, str2, i, j):
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

	return s1[::-1], s2[::-1]



if __name__ == '__main__':
	# with open('./data/fitting_alignment_test.txt') as f:
	# 	str1 = f.readline().strip()
	# 	str2 = f.readline().strip()
	str1 = 'GTTGGATTACGAATCGATATCTGTTTG'
	str2 = 'ACGTCG'
	backtrack, score, row, col = FittingAlignment(str1,str2,1,-1,1)
	s1, s2 = OutputFitting(backtrack,str1,str2,row,col)
	print(score)
	print(s1)
	print(s2)