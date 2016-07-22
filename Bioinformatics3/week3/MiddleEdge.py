# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from AlignmentWithAffineGapPenalties import ReadScoreMatrix

def MiddleNode(str1, str2, scoreMatrix, sigma):
	S = [[0 for i in range(2)] for j in range(len(str1)+1)]
	backtrack = [0 for i in range(len(str1)+1)]
	for i in range(len(str1)+1):
		S[i][0] = -i*sigma
	# S[0][1] = -sigma

	for i in range(1,int(len(str2)/2)+1):
		for j in range(len(str1)+1):
			if j==0:
				S[j][1] = -i*sigma
			else:
				scores = [S[j-1][0]+scoreMatrix[(str1[j-1],str2[i-1])],S[j][0]-sigma,S[j-1][1]-sigma]
				S[j][1] = max(scores)
				backtrack[j] = scores.index(S[j][1])

		if i != int(len(str2)/2):
			S = [[row[1]]*2 for row in S]
	# print([row[1] for row in S])
	return [row[1] for row in S], backtrack


def MiddleEdge(str1, str2, scoreMatrix, sigma):
	source_to_middle = MiddleNode(str1,str2,scoreMatrix,sigma)[0]
	# max_source_to_middle = max(source_to_middle)
	# max_source_to_middle_index = source_to_middle.index(max_source_to_middle)
	# print(source_to_middle)
	middle_to_sink, backtrack = list(map(lambda l: l[::-1],
		MiddleNode(str1[::-1],str2[::-1]+['', '$'][len(str2) % 2 == 1 and len(str2) > 1],scoreMatrix,sigma)))



	scores = list(map(sum, zip(source_to_middle, middle_to_sink)))
	max_middle = max(range(len(scores)), key=lambda i: scores[i])

	# print(middle_to_sink)
	# print(backtrack)
	if max_middle == len(scores) - 1:
		next_node = (max_middle, int(len(str2)/2) + 1)
	else:
		next_node = [(max_middle + 1, int(len(str2)/2) + 1), (max_middle, int(len(str2)/2) + 1), (max_middle + 1, int(len(str2)/2)),][backtrack[max_middle]]
	# if backtrack[-max_source_to_middle_index-1] == 0:
	# 	nextnode = (max_source_to_middle_index+1,int(len(str2)/2)+1)
	# elif backtrack[-max_source_to_middle_index-1] == 1:
	# 	nextnode = (max_source_to_middle_index,int(len(str2)/2)+1)
	# elif backtrack[-max_source_to_middle_index-1] == 2:
	# 	nextnode = (max_source_to_middle_index+1,int(len(str2)/2))
	# return (max_source_to_middle_index, int(len(str2)/2)),backtrack[-max_source_to_middle_index-1]
	return (max_middle, int(len(str2)/2)), next_node



if __name__ == '__main__':
	scoreMatrix = ReadScoreMatrix('BLOSUM62.txt')
	# with open('./data/middle_edge_test.txt') as f:
	# 	str1 = f.readline().strip()
	# 	str2 = f.readline().strip()
	str1 = 'PLEASANTLY'
	str2 = 'MEASNLY'
	print(MiddleEdge(str1[:4],str2[:3],scoreMatrix,5))



