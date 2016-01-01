# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint
from functools import cmp_to_key

def BurrowsWheelerTransformation(text):
	CyclicRotation = [text]
	for i in range(1,len(text)):
		CyclicRotation.append(text[-i:]+text[:-i])
	M_text = sorted(CyclicRotation)
	BWT = [v[-1] for v in M_text]
	BWT = ''.join(BWT)
	return BWT
	# pprint(M_text)

# def BWT(word):
# 	'''Performs a Burrows-Wheeler transform on the given word.'''
#
# 	# Check that the word ends in the out of alphabet character '$'.
# 	word += ['', '$'][word[-1] != '$']
#
# 	# Store the length of the word to save a marginal amount of time, as we'll call the length often.
# 	L = len(word)
#
# 	# A lambda function to get the nth character of the cyclic rotation (to the right) by i characters.
# 	cyclic_rot_index = lambda i, n: word[(n-i) % L]
#
# 	# A lambda function to compare cyclic rotations without generating the entire rotation.
# 	# Use the previously defined lambda function to compare rotation indices.
# 	cyclic_comp = lambda i, j, n=0: [1, -1][cyclic_rot_index(i,n) < cyclic_rot_index(j,n)] if cyclic_rot_index(i,n) != cyclic_rot_index(j,n) else cyclic_comp(i,j,n+1)
# 	cyclic_comp = cmp_to_key(lambda i, j, n=0:
# 							 [1, -1][cyclic_rot_index(i,n) < cyclic_rot_index(j,n)]
# 							 if cyclic_rot_index(i,n) != cyclic_rot_index(j,n) else cyclic_comp(i,j,n+1))
#
# 	# Sort the cyclic rotations based on their shift using the previously defined comparison function.
#
#
# 	cyclic_sort = sorted(range(len(word)), key=cyclic_comp)
#
# 	# Return the last index of each cyclic rotation in the sorted oreder joined into a string.
# 	return ''.join([cyclic_rot_index(i, -1) for i in cyclic_sort])

if __name__ == '__main__':
	# with open('./data/BWT_test.txt') as f:
	# 	text = f.readline().strip()
	text = 'GCGTGCCTGGTCA$'
	print(BurrowsWheelerTransformation(text))
	# print(BWT(text))