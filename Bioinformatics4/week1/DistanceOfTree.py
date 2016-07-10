# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint

def DistanceOfTree(leaves, edges, edge_weight):
	dist = [[0 for i in range(leaves)] for j in range(leaves)]
	pass







if '__name__' == '__main__':
	with open('Distance_Between_Leaves_train.txt') as input:
		leaves = int(input.readline())
		edges, edge_weight = {}, {}
		for pair in [line.strip().split('->') for line in input.readline()]:
			if int(pair[0]) not in edges:
				edges[pair[0]] = pair[1]
			else:
				edges[pair[0]].append(pair[1])
			edge_weight[int[pair[0]],int(pair[1].split(':')[0])] = int(pair[1].split(':')[1])
	pprint(leaves)
	pprint(edges)
	pprint(edge_weight)


