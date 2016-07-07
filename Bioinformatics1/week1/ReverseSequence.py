# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


ReverseDict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}


def ReverseSequence(Sequence):
	result = ""
	for i in range(len(Sequence)-1,-1,-1):
		# print(i)
		result += ReverseDict[Sequence[i]]
	return result