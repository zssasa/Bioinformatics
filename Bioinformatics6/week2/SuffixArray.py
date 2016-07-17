# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'



def SuffixArray(Text):
	suffix = dict()
	for i in range(len(Text)):
		suffix[Text[i:]] = i
	sorted_suffix = sorted(suffix.items(),key=lambda x:x[0])
	return sorted_suffix

if __name__ == '__main__':
	with open('./data/SuffixArray_test.txt') as f:
		Text = f.readline().strip()
	# Text = 'AACGATAGCGGTAGA$'
	arrays = SuffixArray(Text)
	pos = [array[1] for array in arrays]
	print(', '.join(map(str,pos)))
