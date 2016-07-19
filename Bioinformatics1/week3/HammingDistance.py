# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def hamming_distance(str1, str2):
	assert len(str1) == len(str2)
	dist = 0
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			dist += 1
	return dist


if __name__ == '__main__':
	# with open('./data/HammingDistance_test.txt') as f:
	# 	str1 = f.readline().strip()
	# 	str2 = f.readline().strip()
	str1 = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
	str2 = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'
	print(hamming_distance(str1,str2))
