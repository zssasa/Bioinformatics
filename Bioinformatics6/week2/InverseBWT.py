# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def InverseBWT(text):
	inverse_bwt = ""
	lastColumn_map = enumerate_word(text)
	# print(lastColumn_map)
	firstColumn_map = enumerate_word(sorted(text))
	# print(firstColumn_map)
	# last_first = dict()
	last_first = {lastColumn_map[i]:firstColumn_map[i] for i in range(len(text))}

	current_ch = lastColumn_map[0]
	for i in range(len(text)):
		current_ch = last_first[current_ch]
		inverse_bwt += current_ch[0]

	return inverse_bwt[1:]+inverse_bwt[0]


def enumerate_word(word):
	'''
	Enumerates like characters in the order of their appearance for the given word.
	i.e. 'abcbba' returns ['a0', 'b0', 'c0', 'b1', 'b2', 'a1']
	'''

	# Initialize the character count and enumerated character list.
	char_count = {}
	enumerated = []

	# Enumerate like characters.
	for ch in word:
		if ch not in char_count:
			char_count[ch] = 0
		else:
			char_count[ch] += 1
		enumerated.append(ch+str(char_count[ch]))

	return enumerated


if __name__ == '__main__':
	# with open('./data/inverseBWT_test.txt') as f:
	# 	text = f.readline().strip()
	text = 'enwvpeoseu$llt'
	print(InverseBWT(text))

