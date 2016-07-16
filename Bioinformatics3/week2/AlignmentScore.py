# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def AlignmentScore(str1, str2, match_cost, mismatch_cost, indel):
	score = 0
	for i in range(len(str1)):
		if str1[i] == '-' or str2[i] == '-':
			score += indel
		elif str1[i] == str2[i]:
			score += match_cost
		elif str1[i] != str2[i]:
			score += mismatch_cost
	return score

str1 = 'A-C--GTTAC'
str2 = 'ATGCAG---T'
print(AlignmentScore(str1,str2,1,-1,-2))

str1 = 'ATAGCGACGCCT'
str2 = 'ATA-CGATA-CA'
print(AlignmentScore(str1,str2,1,-3,-1))

str1 = 'CTAGTACTACTTGAC'
str2 = 'CTA-TAGT-CTTAAC'
print(AlignmentScore(str1,str2,1,0,-2))

