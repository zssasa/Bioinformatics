# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

import numpy as np
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


def UPGMA(D, n):

	clusters = dict()
	T_node = dict()
	T_edge = dict()
	for i in range(n):
		clusters[i] = 1
		T_node[i] = 0

	# print(clusters)
	def updateD(i,j):
		new = max(list(D.keys())) + 1
		clusters[new] = clusters[i]+clusters[j]
		T_node[new] = (D[i][j])/2
		T_edge[(new,i)] = T_node[new] - T_node[i]
		T_edge[(i,new)] = T_edge[(new,i)]
		T_edge[(new,j)] = T_node[new] - T_node[j]
		T_edge[(j,new)] = T_edge[(new,j)]
		# T_edge[new] = dict()

		# T_edge[new][i] = T_node[new] - T_node[i]
		# T_edge[new][j] = T_node[new] - T_node[j]

		for s in D:
			if s != i and s != j:
				# D[s][new] = (D[s][i]*len(clusters[i])+D[s][j]*len(clusters[j]))/(len(clusters[i])+len(clusters[j]))
				D[s][new] = (D[s][i]*clusters[i]+D[s][j]*clusters[j])/(clusters[i]+clusters[j])
				del D[s][i]
				del D[s][j]
		del D[i]
		del D[j]
		del clusters[i]
		del clusters[j]
		D[new] = dict()
		for s in D:
			if s == new:
				D[new][s] = 0
			else:
				D[new][s] = D[s][new]
		return

	while len(clusters) > 1:
		i,j = minDist(D)
		updateD(i,j)
		# pprint(D)
		# pprint(clusters)
		# pprint(T_node)
	# pprint(D)
	# pprint(clusters)
	# pprint(T_node)
	# pprint(T_edge)
	return T_edge






if __name__ == '__main__':
	with open('./data/UPGMA_test.txt') as f:
		n = int(f.readline().strip())
		Dist = dict()
		for i in range(n):
			Dist[i] = dict()
			line = list(map(int,f.readline().strip().split()))
			for j in range(len(line)):
				Dist[i][j] = line[j]
			# Dist[i] = list(map(int,f.readline().strip().split()))
	# print(Dist)
	# print(minDist(Dist))
	graph = UPGMA(Dist,n)
	# pprint(graph)
	graph_keys = sorted(graph.keys())
	for key in graph_keys:
		print('%d->%d:%.2f' %(key[0],key[1],graph[key]))


