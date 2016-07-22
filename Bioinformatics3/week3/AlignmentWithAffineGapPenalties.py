# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


from pprint import pprint

def ReadScoreMatrix(file):
	scoreMatrix = dict()
	with open(file) as f:
		proteins = f.readline().strip().split()
		for line in f:
			line = line.strip().split()
			for i in range(len(proteins)):
				scoreMatrix[(line[0],proteins[i])] = int(line[i+1])
	return scoreMatrix


def Backtrack(str1, str2, lower, middle, upper, i, j):
	s1 = ''
	s2 = ''
	while i>0 and j>0:
		if middle[i][j] == 3:
			s1 += str1[i-1]
			s2 += str2[j-1]
			i -= 1
			j -= 1
		elif middle[i][j] == 2:
			# s1 += '-'
			# s2 += str2[j-1]
			while upper[i][j] != 2:
				s1 += '-'
				s2 += str2[j-1]
				j -= 1
			s1 += '-'
			s2 += str2[j-1]
			j -= 1
		elif middle[i][j] == 1:
			while lower[i][j] != 2:
				s1 += str1[i-1]
				s2 += '-'
				i -= 1
			s1 += str1[i-1]
			s2 += '-'
			i -= 1
	return s1[::-1],s2[::-1]


def AlignWithAffineGapPenalties(str1, str2, scoreMatrix, sigma, epsilon):
	lower = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	upper = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	middle = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	backtrack_lower = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	backtrack_upper = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	backtrack_middle = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]

	middle[1][0] = -sigma
	lower[1][0] = -sigma
	for i in range(2,len(str1)+1):
		middle[i][0] = middle[i-1][0] - epsilon
		lower[i][0] = lower[i-1][0] - epsilon

	# for i in range(1,len(str1)+1):
	# 	upper[i][0] = -float("inf")

	middle[0][1] = -sigma
	lower[0][1] = -sigma
	for i in range(2,len(str2)+1):
		middle[0][i] = middle[0][i-1] - epsilon
		upper[0][i] = upper[0][i-1] - epsilon

	# for i in range(1,len(str2)+1):
	# 	lower[0][i] = -float("inf")

	for i in range(1,len(str1)+1):
		for j in range(1,len(str2)+1):
			lower[i][j] = max(lower[i-1][j]-epsilon, middle[i-1][j]-sigma)
			upper[i][j] = max(upper[i][j-1]-epsilon, middle[i][j-1]-sigma)
			middle[i][j] = max(lower[i][j], upper[i][j], middle[i-1][j-1]+scoreMatrix[(str1[i-1],str2[j-1])])

			if lower[i][j] == lower[i-1][j]-epsilon:
				backtrack_lower[i][j] = 1 # for down
			elif lower[i][j] == middle[i-1][j]-sigma:
				backtrack_lower[i][j] = 2 # for middle

			if upper[i][j] == upper[i][j-1]-epsilon:
				backtrack_upper[i][j] = 1 # for right
			elif upper[i][j] == middle[i][j-1]-sigma:
				backtrack_upper[i][j] = 2 # for middle

			if middle[i][j] == lower[i][j]:
				backtrack_middle[i][j] = 1 # for lower
			elif middle[i][j] == upper[i][j]:
				backtrack_middle[i][j] = 2 # for upper
			elif middle[i][j] ==  middle[i-1][j-1]+scoreMatrix[(str1[i-1],str2[j-1])]:
				backtrack_middle[i][j] = 3 # for diagonal

	s1,s2 = Backtrack(str1, str2, backtrack_lower,backtrack_middle,backtrack_upper,len(str1),len(str2))

	return middle[len(str1)][len(str2)],s1,s2


if __name__ == '__main__':
	scoreMatrix = ReadScoreMatrix('BLOSUM62.txt')
	with open('./data/alignment_affine_gap_penalties_test.txt') as f:
		str1 = f.readline().strip()
		str2 = f.readline().strip()
	# pprint(scoreMatrix)
	# str1 = 'PRTEINS'
	# str2 = 'PRTWPSEIN'
	s1, s2, s3 = AlignWithAffineGapPenalties(str1,str2,scoreMatrix,11,1)
	print(s1)
	print(s2)
	print(s3)

