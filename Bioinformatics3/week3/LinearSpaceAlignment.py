# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from AlignmentWithAffineGapPenalties import ReadScoreMatrix
from MiddleEdge import MiddleNode
from MiddleEdge import MiddleEdge
from GlobalAlignment import GlobalAlignment


def SpaceEfficientAlignment(str1, str2, scoreMatrix, sigma):
	def LinearSpaceAlignment(top,bottom,left,right):
		# print('top: %d, bottom: %d, left: %d,right: %d' %(top,bottom,left,right))
		if left == right:
			return [str1[top:bottom], '-'*(bottom-top)]
		if top == bottom:
			return ['-'*(right-left), str2[left:right]]
		if bottom - top == 1 or right - left == 1:
			# print(GlobalAlignment(str1[top:bottom], str2[left:right], scoreMatrix, sigma)[:-1])
			return GlobalAlignment(str1[top:bottom], str2[left:right], scoreMatrix, sigma)[:-1]
		# midCol = int((left+right)/2)
		mid_node, next_node = MiddleEdge(str1[top:bottom],str2[left:right],scoreMatrix,sigma)
		# print(midNode)
		# print(midEdge)
		mid_node = tuple(map(sum, zip(mid_node, [top, left])))
		next_node = tuple(map(sum, zip(next_node, [top, left])))
		# midRow = midNode[0]+top
		# midCol = midCol
		# LinearSpaceAlignment(top,tem,left,middle)
		# print(midEdge)
		# new_midRow = midRow
		# new_midCol = midCol
		# if midEdge == 0 or midEdge == 1:
		# 	new_midCol += 1
		# if midEdge == 0 or midEdge == 2:
		# 	new_midRow += 1
		# if midEdge == 0:
		# 	current = [str1[midRow],str2[midCol]]
		# elif midEdge == 1:
		# 	current = ['-','']
		# elif midEdge == 2:
		# 	current = ['','-']
		# print(current)
		# current = [['-', str1[mid_node[0] % len(str1)]][next_node[0] - mid_node[0]], ['-', str2[mid_node[1] % len(str2)]][next_node[1] - mid_node[1]]]
		# print('%d %d %d %d' %(mid_node[0],mid_node[1],next_node[0],next_node[1]))
		if next_node[0]-mid_node[0] == 1 and next_node[1]-mid_node[1]==1:
			current = [str1[mid_node[0]],str2[mid_node[1]]]
		elif next_node[0]-mid_node[0] == 1 and next_node[1]-mid_node[1]==0:
			current = [str1[mid_node[0]],'-']
		elif next_node[0]-mid_node[0] == 0 and next_node[1]-mid_node[1]==1:
			current = ['-',str2[mid_node[1]]]
		A = LinearSpaceAlignment(top,mid_node[0],left,mid_node[1])
		# print(A)
		B = LinearSpaceAlignment(next_node[0],bottom,next_node[1],right)
		# print(B)
		return [A[i]+current[i]+B[i] for i in range(2)]
		# LinearSpaceAlignment(tem,bottom,middle,right)
	s1,s2 = LinearSpaceAlignment(0,len(str1),0,len(str2))
	score = sum([-sigma if '-' in pair else scoreMatrix[pair] for pair in zip(s1, s2)])
	return score,s1,s2

if __name__ == '__main__':
	scoreMatrix = ReadScoreMatrix('BLOSUM62.txt')
	with open('./data/linear_space_alignment_test.txt') as f:
		str1 = f.readline().strip()
		str2 = f.readline().strip()
	# str1 = 'PLEASANTLY'
	# str2 = 'MEANLY'
	sigma = 5
	s = SpaceEfficientAlignment(str1,str2,scoreMatrix,sigma)
	for ss in s:
		print(ss)
	# print(SpaceEfficientAlignment(str1,str2,scoreMatrix,sigma))