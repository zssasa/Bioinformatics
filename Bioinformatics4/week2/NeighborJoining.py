# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'



from pprint import pprint

def minDist(D):
	# if len(D) == 2:
	# 	return
	minD = float("inf")
	for key in D:
		# print(key)
		for s in D[key]:
			if D[key][s] == 0:
				continue
			else:
				if D[key][s]<minD:
					minD = D[key][s]
					i = key
					j = s
					# print(i)
					# print(j)
					# print(minD)
	return i,j

def NeighborJoiningMatrix(D, n):
	# n = len(D)
	D_star = dict()
	TotalDistance = dict()
	for i in D:
		TotalDistance[i] = sum(list(D[i].values()))
	for i in D:
		D_star[i] = dict()
		for j in D[i]:
			if j==i:
				D_star[i][j] = 0
			else:
				D_star[i][j] = (n-2)*D[i][j] - TotalDistance[i] - TotalDistance[j]
	return D_star


def NeighborJoining(D, n):
	# pprint(D)
	if n==2:
		T_edge = dict()
		keys = list(D.keys())
		T_edge[(keys[0],keys[1])] = D[keys[0]][keys[1]]
		T_edge[(keys[1],keys[0])] = D[keys[1]][keys[0]]
		return T_edge

	D_star = NeighborJoiningMatrix(D,n)
	# pprint(D_star)
	i,j = minDist(D_star)
	print(i)
	print(j)
	TotalDistanceOfi = sum(list(D[i].values()))
	TotalDistanceOfj = sum(list(D[j].values()))
	delta = (TotalDistanceOfi-TotalDistanceOfj)/(n-2)
	limbLengthOfi = (delta+D[i][j])/2
	limbLengthOfj = (-delta+D[i][j])/2
	print('%d limb length: %.2f' %(i,limbLengthOfi))
	print('%d limb length: %.2f' %(j,limbLengthOfj))
	new = max(list(D.keys())) + 1
	for s in D:
		if s != i and s != j:
			# print(s)
			D[s][new] = (D[i][s]+D[j][s]-D[i][j])/2
			del D[s][i]
			del D[s][j]
	del D[i]
	del D[j]

	D[new] = dict()
	for s in D:
		if s == new:
			D[new][s] = 0
		else:
			D[new][s] = D[s][new]

	T_edge = NeighborJoining(D,n-1)
	T_edge[(i,new)] = limbLengthOfi
	T_edge[(new,i)] = limbLengthOfi
	T_edge[(j,new)] = limbLengthOfj
	T_edge[(new,j)] = limbLengthOfj

	return T_edge



if __name__ == '__main__':
	# with open('./data/Neighbor_Joining_test.txt') as f:
	with open('./neighborJoining.txt') as f:
		n = int(f.readline().strip())
		Dist = dict()
		for i in range(n):
			Dist[i] = dict()
			line = list(map(int,f.readline().strip().split()))
			for j in range(len(line)):
				Dist[i][j] = line[j]
			# Dist[i] = list(map(int,f.readline().strip().split()))
	print(Dist)
	D_star = NeighborJoiningMatrix(Dist,n)
	pprint(D_star)
	# print(minDist(Dist))
	graph = NeighborJoining(Dist,n)
	# print(graph)
	# graph_keys = sorted(graph.keys())
	# for key in graph_keys:
	# 	print('%d->%d:%.2f' %(key[0],key[1],graph[key]))
	# pprint(graph)



