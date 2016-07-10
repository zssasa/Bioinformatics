# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

# from pprint import pprint



def dfs_path(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		for next in set(graph[vertex]) - set(path):
			# print(next)
			if next == goal:
				yield path+[next]
			else:
				# print(stack)
				stack.append((next,path+[next]))
				# print(stack)

def distance(edge_weight, path):
	dist = 0
	for i in range(len(path)-1):
		dist += edge_weight[(int(path[i]),int(path[i+1]))]
	return dist

def DistanceOfTree(leaves, edges, edge_weight):
	dist = [[0 for i in range(leaves)] for j in range(leaves)]
	for i in range(leaves-1):
		for j in range(i+1,leaves):
			dist[i][j] = distance(edge_weight,list(dfs_path(edges,i,j))[0])
			dist[j][i] = dist[i][j]
	return dist



if __name__ == '__main__':
	with open('./data/Distance_Between_Leaves_test.txt') as input:
		leaves = int(input.readline())
		edges, edge_weight = {}, {}
		for pair in [line.strip().split('->') for line in input.readlines()]:
			if int(pair[0]) not in edges:
				edges[int(pair[0])] = [int(pair[1].split(':')[0])]
			else:
				edges[int(pair[0])].append(int(pair[1].split(':')[0]))
			edge_weight[int(pair[0]),int(pair[1].split(':')[0])] = int(pair[1].split(':')[1])
	# print(leaves)
	# print(edges)
	# print(edge_weight)
	# print(list(dfs_path(edges,0,3)))
	dist = DistanceOfTree(leaves, edges, edge_weight)
	for i in range(leaves):
		for j in range(leaves):
			print(dist[i][j], end=" ")
		print('\n',end="")


