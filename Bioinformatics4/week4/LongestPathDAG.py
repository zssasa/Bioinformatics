# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from collections import defaultdict

def ParseEdge(line):
	start, tem = line.split('->')
	end, dist = tem.split(':')
	return int(start), int(end), int(dist)


def Graph(source, sink, edges):
	G = defaultdict(list)
	# G = []
	for edge in edges:
		start,end,dist = ParseEdge(edge)
		# G.append((start,[(end,dist)]))
		# G[start].append(end)
		G[start].append((end,dist))
		# G[start][end] = dist
	for i in range(sink-source+1):
		if i not in G:
			# G[i] = {}
			G[i] = []
	G_list = [(k,v) for k,v in G.items()]
	return G_list


def TopologicalSort(graph_unsorted):
	graph_sorted = []
	graph_unsorted = dict(graph_unsorted)
	while graph_unsorted:
		acyclic = False
		for node in list(graph_unsorted.keys()):
		#for node,edges in graph_unsorted.items():
			edges = graph_unsorted[node]
			for edge in edges:
				#print(edge)
				if edge[0] in graph_unsorted:
					break
			else:
				acyclic = True
				del graph_unsorted[node]
				graph_sorted.append((node,edges))

		if not acyclic:
			raise RuntimeError("A cyclic dependency occurred")
	return graph_sorted

def LongestPathDAG(source, sink, graph):
	length_to = [0] * (sink-source+1)
	for node,edges in graph:
		# print(node)
		# print(edges)
		for edge in edges:
			if length_to[node] <= length_to[edge[0]] + edge[1]:
				length_to[node] = length_to[edge[0]] + edge[1]
		else:
			continue
	return length_to
