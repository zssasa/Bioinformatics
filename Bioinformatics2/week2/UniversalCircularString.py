# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


from itertools import product
from StringReconstruction import DeBrujinFromKmers, PathToStr
from EulerianCycle import EulerianCycle

def UniversalCircularString(k):
	kmers = [''.join(x) for x in product('01',repeat=k)]
	# print(kmers)
	graph = DeBrujinFromKmers(kmers)
	str = EulerianCycle(graph)
	return str



if __name__ == '__main__':
	k = 8
	s = UniversalCircularString(k)
	# print(s)
	# print(PathToStr(s))
	print(PathToStr(s)[:-k+1])


