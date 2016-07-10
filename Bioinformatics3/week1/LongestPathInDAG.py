# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def TopologicalSort(graph):
	graph = set(graph)
	ordering = []

	# all nodes don't have predecessor
	candidates = list({edge[0] for edge in graph} - {edge[1] for edge in graph})
	# print(candidates)
	while(len(candidates) != 0):
		ordering.append(candidates[0])

		tem_nodes = []
		for edge in filter(lambda e:e[0] == candidates[0], graph):
			tem_nodes.append(edge[1])
			graph.remove(edge)

		for node in tem_nodes:
			if node not in {edge[1] for edge in graph}:
				candidates.append(node)

		candidates = candidates[1:]

	return ordering


def LongestPath(graph, edges, source, sink):
	top_order = TopologicalSort(graph.keys())
	top_order = top_order[top_order.index(source)+1:top_order.index(sink)+1]

	S = {node:-100 for node in {edge[0] for edge in graph.keys()} | {edge[1] for edge in graph.keys()}}
	S[source] = 0
	backtrack = {node:None for node in top_order}

	for node in top_order:
		try:
			S[node], backtrack[node] = max(map(lambda e: [S[e[0]] + graph[e], e[0]], filter(lambda e: e[1] == node, graph.keys())), key=lambda p:p[0])
		# ValueError occurs if max() is empty, i.e. the given node has no predecessor.  This is fine, as top_order can include unrealted vertices.
		# Ignore such nodes, as they will not factor into the longest path from source to sink.
		except ValueError:
			pass
	path = [sink]
	while path[0] != source:
		path = [backtrack[path[0]]] + path

	return S[sink], path


if __name__ == '__main__':
	# source = 0
	# sink = 4
	# lines = ['0->1:7','0->2:4','2->3:2','1->4:1','3->4:3']
	with open('./data/longest_path_in_DAG_test.txt') as input_data:
		source, sink = [int(input_data.readline()) for repeat in range(2)]
		edges, edge_weight = {}, {}
		for pair in [line.strip().split('->') for line in input_data.readlines()]:
			if int(pair[0]) not in edges:
				edges[int(pair[0])] = [int(pair[1].split(':')[0])]
			else:
				edges[int(pair[0])].append([int(pair[1].split(':')[0])])
			edge_weight[int(pair[0]), int(pair[1].split(':')[0])] = int(pair[1].split(':')[1])

	# ordering = TopologicalSort(edge_weight.keys())
	# print(ordering)
	# ordering = ordering[ordering.index(source)+1:ordering.index(sink)+1]
	# print(ordering)
	length, path = LongestPath(edge_weight, edges, source, sink)
	print(length)
	path = '->'.join(map(str, path))
	print(path)
