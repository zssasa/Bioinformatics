# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint

_end = '$'
def make_trie(words):
	"""
	CODE CHALLENGE: Solve the Trie Construction Problem.
	Input: A collection of strings Patterns.
	Output: The adjacency list corresponding to Trie(Patterns), in the following format. If
	Trie(Patterns) has n nodes, first label the root with 0 and then label the remaining nodes with
	the integers 1 through n - 1 in any order you like. Each edge of the adjacency list of
	Trie(Patterns) will be encoded by a triple: the first two members of the triple must be the
	integers labeling the initial and terminal nodes of the edge, respectively; the third member
	of the triple must be the symbol labeling the edge.
	"""
	root = dict()
	for word in words:
		# print(word)
		# print(type(word))
		current_dict = root
		for letter in word:
			# print(letter)
			current_dict = current_dict.setdefault(letter, {})
		current_dict = current_dict.setdefault(_end, _end)
	return root

def trie_tostr(root):
	s = []
	def dump_leaf(curr,parent_id):
		current_id = parent_id + 1
		for key, value in curr.items():
			if (value == _end):
				continue
			s.append(str(parent_id)+'->'+str(current_id)+':'+key)
			current_id = dump_leaf(value,current_id)
		return current_id
	dump_leaf(root,0)
	return "\n".join(s)

if __name__ == '__main__':
	with open('./data/trie_train.txt') as f:
		words = f.read().splitlines()
		t = make_trie(words)
		s = trie_tostr(t)

		pprint(t)
		print(s)