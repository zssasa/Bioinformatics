# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def StringComposition(k, sequence):
	result = []
	for i in range(len(sequence)-k+1):
		result.append(sequence[i:i+k])
	return result
