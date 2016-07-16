# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


from pprint import pprint


def OverlapAlignment(str1, str2):
	S = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	BackTrack = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]

	for i in range(1,len(str1)+1):
		S[i][0] = 0
	for j in range(1,len(str2)+1):
		S[0][j] = S[0][j-1]-1
	for i in range(1,len(str1)+1):
		for j in range(1,len(str2)+1):
			if str1[i-1] == str2[j-1]:
				cost = 1
			else:
				cost = -2
			S[i][j] = max(S[i-1][j]-2,S[i][j-1]-2,S[i-1][j-1]+cost)
			if S[i][j] == S[i-1][j]-2:
				BackTrack[i][j] = 2
			elif S[i][j] == S[i][j-1]-2:
				BackTrack[i][j] = 3
			elif S[i][j] == S[i-1][j-1]+cost:
				BackTrack[i][j] = 1
	# pprint(S)
	# pprint(BackTrack)
	row = S[-1]
	col = row.index(max(row))
	return BackTrack,S[len(str1)][col],len(str1),col

def OutputOverlap(backtrack, str1, str2, i, j):
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
	with open('./data/overlap_alignment_test.txt') as f:
		str1 = f.readline().strip()
		str2 = f.readline().strip()
	# str1 = 'PAWHEAE'
	# str2 = 'HEAGAWGHEE'
	backtrack, score, row, col = OverlapAlignment(str1,str2)
	s1, s2 = OutputOverlap(backtrack,str1,str2,row,col)
	print(score)
	print(s1)
	print(s2)
