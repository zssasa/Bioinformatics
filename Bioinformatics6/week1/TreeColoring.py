# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'



def TreeColoring(edge_lines, node_lines):
	tree_adj = [None] * len(edge_lines)
	tree_color = {}

	for line in edge_lines:
		parse = line.strip().split(' -> ')
		# print(parse)
		if parse[1] != '{}':
			parent_id = int(parse[0])
			child_ids = list(map(int,parse[1].split(',')))
			tree_adj[parent_id] = child_ids
	# print(tree_adj)
	for line in node_lines:
		parse = line.strip().split(': ')
		node_id = int(parse[0])
		if parse[1] ==  'red':
			tree_color[node_id] = 1
		if parse[1] == 'blue':
			tree_color[node_id] = 2
	# print(tree_color)
	def color_node(current_id):
		# print(current_id)
		if current_id in tree_color:
			return tree_color[current_id]
		children = tree_adj[current_id]
		assert children is not None
		color = 0
		for child in children:
			if child in tree_color:
				color |= tree_color[child]
			else:
				color |= color_node(child)
		# tree_color[current_id] = color
		return color

	# print(len(tree_adj))
	# map(color_node,list(range(len(tree_adj))))

	# print(tree_color)
	def colored_node(v):
		if v==1:
			return 'red'
		elif v==2:
			return 'blue'
		else:
			return 'purple'
	# def colored_node(k,v):
	# 	if v == 1:
	# 		return str(k)+': red'
	# 	elif v == 2:
	# 		return str(k)+': blue'
	# 	elif v == 3:
	# 		return str(k)+': purple'
	# 	else:
	# 		print('weird color value (',str(v),') here, shall not happen')

	tree_coloring = {}
	for i in range(len(tree_adj)):
		tem = color_node(i)
		tree_coloring[i] = colored_node(tem)
	# print(tree_coloring)
	# color_list = sorted([colored_node(k,v) for k,v in tree_coloring.items()])
	# return color_list
	# return '\n'.join(color_list)
	return tree_coloring


if __name__ == '__main__':
	with open('./data/TreeColoring_test.txt') as f:
		l = f.read().splitlines()
		i = l.index('-')
		edge_lines = l[:i]
		node_lines = l[i+1:]
	# print(edge_lines)
	# print(node_lines)
	s = TreeColoring(edge_lines,node_lines)
	for node in s:
		print(str(node)+': '+s[node])


