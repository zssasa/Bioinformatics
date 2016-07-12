# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from SuffixTree import SuffixTree
from pprint import pprint

def longest_shared_substring(text1, text2):
	# get all edges and colors if possible
	def dfs_nodes(current_dict):
		if type(current_dict) != dict:
				return
		for key,child_dict in current_dict.items():
			dicts.append(child_dict)
			# label = text[key[0]:key[1]]
			label = key
			labels.append(label)

			if label[-1] == '$':
				if '#' in label:
					colors.append(1)
				else:
					colors.append(2)
			else:
				colors.append(0)
			dfs_nodes(child_dict)
		return


	def dfs_color(current_id):
		if colors[current_id] > 0:
			return colors[current_id]
		current_list = adjacency[current_id]
		assert len(current_list) > 0
		color = 0
		for child_id in current_list:
			if colors[child_id] > 0:
				color |= colors[child_id]
			else:
				color |= dfs_color(child_id)
		colors[current_id] = color
		return color

	def dfs_longest(current_id,prefix):
		assert colors[current_id] > 0
		candidate = prefix + labels[current_id]
		if (colors[current_id] == 3):
			current_list = adjacency[current_id]
			assert len(current_list) > 0
			for child_id in current_list:
				dfs_longest(child_id, candidate)
			if len(candidate) > len(longests[-1]):
				longests.append(candidate)
		return

	# def dfs_shortest(current_id):
	# 	print(current_id)
	# 	assert colors[current_id] > 0
	# 	if (colors[current_id] != 3):
	# 		if len(labels[current_id]) < len(shortest[-1]) and (labels[current_id] != '#') and (labels[current_id] != '$'):
	# 			shortest.append(labels[current_id])
	# 	if (colors[current_id] ==3):
	# 		current_list = adjacency[current_id]
	# 		for child_id in current_list:
	# 			dfs_shortest(child_id)
	# 	return


	text = text1+'#'+text2+'$'
	root = SuffixTree(text)
	pprint(root)
	# print()
	# len dicts/labels/colors = len nodes
	# labels = all edges or nodes
	#dicts all sub dict
	dicts = [root]
	colors = [0]
	labels = ['']
	dfs_nodes(root)
	# pprint(dicts)
	# print()
	# print(colors)
	# print()
	# pprint(labels)
	# print()
	# print(len(text))
	print(len(labels))

	adjacency = []
	for d in dicts:
		if type(d) == int:
			adjacency.append([])
		else:
			adjacency.append([dicts.index(v) for v in d.values()])
	# print(adjacency)

	list(map(dfs_color,list(range(len(colors)))))
	# print(colors)

	# longests=['',]
	root_id = dicts.index(root)
	# dfs_longest(root_id,'')

	if len(text1)<=len(text2):
		shortest = [text1+'#',]
	else:
		shortest = [text2+'$',]
	for i in range(len(colors)):
		if colors[i] == 2:
			if len(labels[i]) < len(shortest[-1]) and labels[i] != '$':
				shortest.append(labels[i])
	# dfs_shortest(root_id)
	# return longests[-1]
	for i in range(len(colors)):
		print('%s : %d' %(labels[i],colors[i]))
	return shortest[-1]


if __name__ == '__main__':
	# with open('./data/LongestSharedSubstring_test.txt') as f:
	# 	text1 = f.readline().strip()
	# 	text2 = f.readline().strip()
	# text1 = 'TCGGTAGATTGCGCCCACTC'
	# text2 = 'AGGGGCTCGCAGTGTAAGAA'
	# text1 = 'CCAAGCTGCTAGAGG'
	# text2 = 'CATGCTGGGCTGGCT'
	# text1 = 'panama'
	# text2 = 'bananas'
	text1 = 'ABABC'
	text2 = 'EFEFG'
	print(longest_shared_substring(text1,text2))
