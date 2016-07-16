# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from StringReconstruction import DeBrujinFromKmers


def OneInOneOut(node, graph):
	if node not in graph:
		return False
	if len(graph[node]) != 1:
		return False
	outNodes = []
	for edge in graph.values():
		outNodes.extend(edge)
	# print(outNodes.count(node))
	if outNodes.count(node) != 1:
		return False

	return True



def IsolatedCycle(graph,InNode):
	path = []
	visited = dict()
	# visited = [None] * (max(list(graph.keys()))+1)
	for key in graph:
		visited[key] = None
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
	# return [cycle]




def NonBranching(graph):
	paths = list()
	for v in graph.keys():
		if not OneInOneOut(v,graph):
			if len(graph[v]) > 0:
				for w in graph[v]:
					NonBranchingPath = [v,w]
					while OneInOneOut(w,graph):
						NonBranchingPath.extend(graph[w])
						w = graph[w][0]
					paths.append(NonBranchingPath)
	InNode = set()
	for path in paths:
		InNode = InNode | set(path)
	paths.extend(IsolatedCycle(graph,InNode))
	return paths

def ContigFromPath(path):
	contigs = []
	for s in path:
		if len(s) == 1:
			contigs.append(s)
		else:
			contig = s[0]
			for i in range(1,len(s)):
				contig += s[i][-1]
			contigs.append(contig)
	return contigs

if __name__ == '__main__':
	# with open('./data/contig_generation_train.txt') as f:
	with open('./data/ContigGeneration_test.txt') as f:
	# with open('./data/ContigGeneration_train.txt') as f:
		texts = [text.strip() for text in f.readlines()]
	# 	texts = f.readlines()
	# texts = [text.strip() for text in texts]
	graph = DeBrujinFromKmers(texts)

	path = NonBranching(graph)
	# print(path)
	contigs = ContigFromPath(path)
	# print(len(path))
	# print(contigs)
	contigs = sorted(contigs)
	print('\n'.join(contigs))
	# print(len(contigs))