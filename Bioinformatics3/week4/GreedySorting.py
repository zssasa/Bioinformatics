# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

import copy


def GreedySorting(P):
	approxReversalDistance = 0
	permutations = []
	for i in range(1,len(P)+1):
		if P[i-1] != i and P[i-1] != -i:
			index = 0
			if i in P:
				index = P.index(i)
			elif -i in P:
				index = P.index(-i)
			tem = P[i-1:index+1]
			tem = [-k for k in tem]
			P[i-1:index+1] = tem[::-1]
			# print(P)
			permutations.append(copy.copy(P))
			# print(permutations)
			approxReversalDistance += 1
		if P[i-1] == -i:
			P[i-1] = i
			permutations.append(copy.copy(P))
			approxReversalDistance += 1
	return approxReversalDistance,permutations


def Breakpoints(P):
	adj = 0
	# bp = 0
	for i in range(len(P)-1):
		if P[i+1]-P[i] == 1:
			# bp += 1
			adj += 1
	if P[0] == 1:
		adj += 1
	if P[-1] == len(P):
		adj += 1
	return len(P)+1-adj


if __name__ == '__main__':
	# with open('./data/GreedySorting_train.txt') as f:
	with open('./data/NumberOfBreakpoints_train.txt') as f:
		P = f.readline().strip()
	P = P[1:-1]
	P = P.split()
	# print(P)
	P = [int(pp) for pp in P]
	# P = [-3, +4, +1, +5, -2]
	# a, permutations = GreedySorting(P)
	# print(a)
	# for p in permutations:
	# 	str_p = ['+'+str(pp) if pp>0 else str(pp) for pp in p]
	# 	print('(%s)' %' '.join(str_p))
	print(Breakpoints(P))



