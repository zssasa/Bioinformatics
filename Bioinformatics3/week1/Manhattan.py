# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

def Manhattan(size, down, right):
	# n:row m:col
	n, m = size
	# Path = [[0] * (n+1)] * (m+1)
	Path = [[0 for i in range(m+1)] for j in range(n+1)]
	print(Path)

	for i in range(1,n+1):
		Path[i][0] = Path[i-1][0] + down[i-1][0]
	#print(Path)
	for i in range(1,m+1):
		Path[0][i] = Path[0][i-1] + right[0][i-1]

	for i in range(1,n+1):
		for j in range(1,m+1):
			Path[i][j] = max(Path[i-1][j]+down[i-1][j],Path[i][j-1]+right[i][j-1])

	return Path



