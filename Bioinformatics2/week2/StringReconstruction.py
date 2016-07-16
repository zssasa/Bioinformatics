# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


from EulerianPath import EulerianPath

def DeBrujinFromKmers(patterns):
	result = dict()
	for pattern in patterns:
		if pattern[:-1] in result:
			result[pattern[:-1]].append(pattern[1:])
		else:
			result[pattern[:-1]] = [pattern[1:]]

	return result

def PathToStr(path):
	str = path[0]
	for i in range(1,len(path)):
		str += path[i][-1]
	return str

if __name__ == '__main__':
	with open('./data/problemset1.txt') as f:
	# with open('./data/StringReconstruction_test.txt') as f:
		k = int(f.readline().strip())
		patterns = f.readlines()
	patterns = [pattern.strip() for pattern in patterns]
	# print(patterns)
	# with open()
	# k = 4
	# patterns = ['CTTA','ACCA','TACC','GGCT','GCTT','TTAC']
	graph = DeBrujinFromKmers(patterns)
	# print(graph)
	s = EulerianPath(graph)
	# print(s)
	print(PathToStr(s))