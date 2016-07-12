# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from Trie import make_trie

_end = '$'

def TrieMatching(Text, words):
	t = make_trie(words)
	pos = [i for i in range(len(Text)) if PrefixTrieMatching(Text[i:], t)]
	return pos

def PrefixTrieMatching(Text, trie):
	candidates = trie.keys()
	if _end in candidates:
		return True
	if not Text:
		return False
	letter = Text[0]
	suffix = Text[1:]
	if letter in candidates:
		return PrefixTrieMatching(suffix,trie[letter])
	return False

if __name__ == '__main__':
	with open('./data/TrieMatching_test.txt') as f:
		Text = f.readline()
		words = f.read().splitlines()
	s=TrieMatching(Text,words)
	for ss in s:
		print(ss,end=' ')