# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


from pprint import pprint
from EulerianCycle import EulerianCycle

def EulerianPath(graph):

	def UnbalancedNode(graph):
		# start = []
		outNodes = set(graph.keys())
		inNodes = []
		for node in outNodes:
			inNodes.extend(graph[node])
		inNodes = set(inNodes)
		# pprint(inNodes)
		# pprint(outNodes)
		end = list(inNodes - outNodes)[0]
		outDegree = dict()
		for node in outNodes:
			outDegree[node] = len(graph[node])
		inDegree = dict()
		for node in graph.keys():
			for inNode in graph[node]:
				inDegree.setdefault(inNode,0)
				inDegree[inNode] += 1
		# pprint(outDegree)
		# pprint(inDegree)
		for node in outDegree:
			if node not in inDegree:
				start = node
				break
			if outDegree[node] > inDegree[node]:
				start = node
		return start,end

	start,end = UnbalancedNode(graph)
	if end in graph:
		graph[end].append(start)
	else:
		graph[end] = [start]
	path = EulerianCycle(graph)
	# print(path)
	divide_point = list(filter(lambda i: path[i:i+2] == [end, start], range(len(path)-1)))[0]
	path = path[divide_point+1:] + path[1:divide_point+1]

	return path


if __name__ == '__main__':
	graph = dict()
	count = 0
	with open('./data/eulerian_path_test.txt') as f:
		for line in f.readlines():
			node, edge = line.split(' -> ')
			graph[int(node)] = list(map(int,edge.split(',')))
			count += len(graph[int(node)])
	# print(count)
	# pprint(graph)
	# s = EulerianPath(graph)
	# print(s)
	# print(len(s))
	# print(s)
	print('->'.join(map(str,EulerianPath(graph))))