# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint
_end = '$'

def SuffixTrieConstruction(Text):
	root = dict()
	for i in range(len(Text)):
		CurrentNode = root
		word = Text[i:]
		# print(word)
		for letter in word:
			# print(letter)
			if letter == _end:
				value = i
			else:
				value = {}
			CurrentNode = CurrentNode.setdefault(letter,value)
	return root


# def SuffixTreeConstruction(Text):
# 	root = SuffixTrieConstruction(Text)
# 	pass


# def FindNonBranchingPath(label, current_dict):
# 	while (type(current_dict) == dict) and (len(list(current_dict.keys())) ==1):
# 		letter = list(current_dict.keys())[0]
# 		label += letter
# 		if (letter == _end):
# 			return (label, current_dict[letter])
# 		current_dict = current_dict[letter]
# 	return label, current_dict
#
# def FactorNonBranchingPath(current_dict):
# 	if type(current_dict) != dict:
# 		return current_dict
# 	labels = current_dict.keys()
# 	for label in labels:
# 		l,d = FindNonBranchingPath(label, current_dict[label])
# 		current_dict.pop(label)
# 		current_dict[l] = d
# 		FactorNonBranchingPath(d)
# 	return current_dict


def EdgeLabel(Text):
	root = SuffixTree(Text)
	s= []
	def DFS(current_dict):
		if type(current_dict) != dict:
			return
		for label in current_dict.keys():
			s.append(label)
			DFS(current_dict[label])
		return
	DFS(root)
	return s

def SuffixTree(Text):
	def FindNonBranchingPath(label, current_dict):
		while (type(current_dict) == dict) and (len(list(current_dict.keys())) ==1):
			letter = list(current_dict.keys())[0]
			label += letter
			if (letter == _end):
				return (label, current_dict[letter])
			current_dict = current_dict[letter]
		return label, current_dict

	def FactorNonBranchingPath(current_dict):
		if type(current_dict) != dict:
			return
		labels = current_dict.keys()
		for label in labels:
			l,d = FindNonBranchingPath(label, current_dict[label])
			current_dict.pop(label)
			current_dict[l] = d
			FactorNonBranchingPath(d)
		return

	root = SuffixTrieConstruction(Text)
	FactorNonBranchingPath(root)
	return root

if __name__ == '__main__':
	Text = 'ATAAATG$'
	# Text = 'anana$'
	# s = SuffixTrieConstruction(Text)
	# pprint(s)
	# pprint(FactorNonBranchingPath(s))
	# pprint()
	# with open('./data/dataset_296_4-5.txt') as f:
	# 	Text = f.readline().strip()
	# print(Text)
	# print(type(Text))
	# print(len(Text))
	# print(Text[855])
	# 	pass
	pprint(SuffixTree(Text))
	# s = SuffixTree(Text)
	s = EdgeLabel(Text)
	for edge in s:
		print(edge)

