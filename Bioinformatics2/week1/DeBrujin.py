# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def DeBrujinFromText(k, Text):
	result = dict()
	for i in range(len(Text)-k+1):
		if Text[i:i+k-1] in result:
			result[Text[i:i+k-1]].append(Text[i+1:i+k])
		else:
			result[Text[i:i+k-1]] = [Text[i+1:i+k]]

	return result


def DeBrujinFromKmers(patterns):
	result = dict()
	for pattern in patterns:
		if pattern[:-1] in result:
			result[pattern[:-1]].append(pattern[1:])
		else:
			result[pattern[:-1]] = [pattern[1:]]

	return result

