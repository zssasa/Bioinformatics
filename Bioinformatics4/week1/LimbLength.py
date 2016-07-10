# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint




def LimbLength(dist, target):
	n = len(dist)
	lim_length = float("inf")
	for i in range(n):
		# just choose a i not target
		# if i != target:
		for j in range(n):
			if i != target and j != target:
				tem = (dist[i][target]+dist[j][target]-dist[i][j])/2
				if tem < lim_length:
					lim_length = tem
	return int(lim_length)







if __name__ == '__main__':
	# with open('./data/Limb_length_test.txt') as input:
	with open('./data/test.txt') as input:

		n = int(input.readline())
		target = int(input.readline())
		dist = []
		for line in input.readlines():
			dist.append(list(map(int,line.split(' '))))
	print(dist)
	print(len(dist))
	print(LimbLength(dist, target))