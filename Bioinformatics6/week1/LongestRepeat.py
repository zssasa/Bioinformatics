# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


from SuffixTree import SuffixTree


def LongestRepeat(Text):
	root = SuffixTree(Text+'$')

	def dfs(root, word):
		if (len(root.keys()))>1 and (len(longest[-1])<len(word)):
			longest.append(word)

		for key,value in root.items():
			if type(value) == dict:
				# label = key
				dfs(value,word+key)
		return

	longest = ['',]
	dfs(root,'')
	return longest[-1]



if __name__ == '__main__':
	with open('./data/LongestRepeat_test.txt') as f:
		Text = f.readline().strip()
	# Text = 'ATATCGTTTTATCGTT'
	print(LongestRepeat(Text))