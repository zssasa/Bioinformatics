# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint


def EulerianCycle(graph):
	current_node = list(graph.keys())[0]
	path = []
	# path = [current_node]

	def FormCycle(node):
		# print(node)
		cycle = [node]
		while True:
			# print(node in graph)
			# print(graph[node])
			cycle.append(graph[node].pop())
			# print(cycle)
			if len(graph[node]) == 0:
				del graph[node]
			# print(graph)
			if cycle[-1] in graph:
				node = cycle[-1]
			else:
				break
			# print(node)
		return cycle

	path.extend(FormCycle(current_node))
	while len(graph)>0:
		for i in range(len(path)):
			if path[i] in graph:
				# print(path[i])
				# print(type(path[i]))
				# print(graph[path[i]])
				current_node = path[i]
				cycle = FormCycle(current_node)
				path = path[:i] + cycle +path[i+1:]
				# break
	return path


if __name__ == '__main__':
	graph = dict()
	count = 0
	with open('./data/eulerian_cycle_test.txt') as f:
		for line in f.readlines():
			node, edge = line.split(' -> ')
			graph[int(node)] = list(map(int,edge.split(',')))
			count += len(graph[int(node)])
	# print(len(graph))
	# print(count)
	# pprint(graph)
	# print(graph[0])
	# s = EulerianCycle(graph)
	# print(len(s))
	# print(s)
	print('->'.join(map(str,EulerianCycle(graph))))