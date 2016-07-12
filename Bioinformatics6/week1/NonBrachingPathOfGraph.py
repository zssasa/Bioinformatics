# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint
import sys
# def AdjToDict(lines):
# 	root = dict()
# 	for line in lines:
# 		current_dict = root
# 		u,v = line.split('->')
# 		current_dict = current_dict.setdefault(u,v)



def adjToGraph(lines):
	graph = dict()
	for line in lines:
		u,v = line.split(' -> ')
		graph.setdefault(int(u),list(map(int,v.split(','))))
	return graph

def OneInOneOut(node, graph):
	# print(node)
	# print(type(node))
	if node not in graph:
		return False

	if len(graph[node]) != 1:
		return False

	In = 0
	for v in graph:
		if v!=node:
			if node in graph[v]:
				In += 1
	if In != 1:
		return False

	return True

def dfs_visited():
	pass



def IsolatedCycle(graph,InNode):
	path = []
	visited = [None] * (max(list(graph.keys()))+1)
	for node in graph:
		cycle = list()
		if node in InNode:
			continue
		if visited[node]:
			continue
		while(OneInOneOut(node,graph)) and (OneInOneOut(graph[node][0],graph)):
			if not visited[node]:
				visited[node] = True
				cycle.append(node)
			if not visited[graph[node][0]]:
				visited[graph[node][0]] = True
				cycle.append(graph[node][0])
			if graph[graph[node][0]][0] in cycle:
				break
			else:
				node = graph[node][0]
		cycle.append(cycle[0])
		path.append(cycle)
	# print(path)
	return path




def NonBranching(graph):

	paths = list()
	for v in graph.keys():
		if not OneInOneOut(v,graph):
			if len(graph[v]) > 0:
				for w in graph[v]:
					NonBranchingPath = [v,w]
					# print(w)
					# print(type(w))
					while OneInOneOut(w,graph):
						NonBranchingPath.extend(graph[w])
						w = graph[w][0]
					paths.append(NonBranchingPath)
	InNode = set()
	for path in paths:
		InNode = InNode | set(path)
	# print(InNode)
	# InNode = set([path for path in paths])
	# print(InNode)
	paths.extend(IsolatedCycle(graph,InNode))
	return paths

if __name__ == '__main__':
	with open('./data/NonBrachingOfGraph_test.txt') as f:
		lines = f.readlines()
	# lines = ['1 -> 2','2 -> 3','3 -> 4,5', '6 -> 7', '7 -> 6']
	graph = adjToGraph(lines)
	# sys.setrecursionlimit(len(list(graph.keys())) + 100)

	# pprint(graph)
	# print(max(list(graph.keys())))
	paths = NonBranching(graph)
	# pprint(paths)
	# pprint(set(paths))
	for path in paths:
		print(' -> '.join(map(str,path)))