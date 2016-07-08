# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

# 1 for match; 2 for down; 3 for right

def LGSBackTrack(v, w):
	S = [[0 for i in range(len(w)+1)] for j in range(len(v)+1)]
	BackTrack = [[0 for i in range(len(w)+1)] for j in range(len(v)+1)]

	for i in range(1,len(v)+1):
		for j in range(1,len(w)+1):
			S[i][j] = max(S[i-1][j],S[i][j-1],S[i-1][j-1]+1*(v[i-1]==w[j-1]))
			if S[i][j] == S[i-1][j]:
				BackTrack[i][j] = 2
			elif S[i][j] == S[i][j-1]:
				BackTrack[i][j] = 3
			elif S[i][j] == S[i-1][j-1]+1:
				BackTrack[i][j] = 1
	return BackTrack


def OutputLGS(backtrack, v, i, j):
	if i==0 or j==0:
		return 1
	elif backtrack[i][j] == 2:
		return OutputLGS(backtrack, v, i-1, j)
	elif backtrack[i][j] == 3:
		return OutputLGS(backtrack, v, i, j-1)
	elif backtrack[i][j] == 1:
		OutputLGS(backtrack, v, i-1, j-1)
		print(v[i])
	else:
		return 1

