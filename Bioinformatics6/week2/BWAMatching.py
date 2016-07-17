# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from InverseBWT import enumerate_word

def BWAMatching(LastColumn, Pattern, LastToFirst):
	top = 0
	bottom = len(LastColumn) - 1

	while top<=bottom:
		if Pattern:
			symbol = Pattern[-1]
			Pattern = Pattern[:-1]
			if symbol in LastColumn[top:bottom+1]:
				top_index = top + LastColumn[top:bottom+1].index(symbol)
				# print(top_index)
				bottom_index = bottom - LastColumn[top:bottom+1][::-1].index(symbol)
				top = LastToFirst[top_index]
				bottom = LastToFirst[bottom_index]
			else:
				return 0
		else:
			return bottom-top+1


def get_pattern_count(text, patterns):
	lastColumn_map = enumerate_word(text)
	firstColumn_map = enumerate_word(sorted(text))
	last_to_first = {i:firstColumn_map.index(lastColumn_map[i]) for i in range(len(text))}
	# print(last_to_first)
	return [BWAMatching(text,pattern,last_to_first) for pattern in patterns]


if __name__ == '__main__':
	with open('./data/BWMatching_test.txt') as f:
		text = f.readline().strip()
		patterns = f.readline().strip().split()
	# text = 'TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC'
	# patterns = ['CCT','CAC', 'GAG', 'CAG', 'ATC']
	# print(get_pattern_count(text,patterns))
	print(' '.join(map(str,get_pattern_count(text,patterns))))




