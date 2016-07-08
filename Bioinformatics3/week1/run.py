# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from DPChange import DPChange
from Manhattan import Manhattan
from LCS import LGSBackTrack
from LCS import OutputLGS

# import sys
# lines = sys.stdin.read().splitlines()


# print(lines[1])
# print(type(lines[1]))
# print(list(lines[1]))
# print(list(map(int,lines[1].split(','))))

# print(DPChange(int(lines[0]),list(map(int,lines[1].split(',')))))

# size=[4,4]
#
# down=[[1,0,2,4,3],[4,6,5,2,1],[4,4,5,2,1],[5,6,8,5,3]]
#
# right=[[3,2,4,0],[3,2,4,2],[0,7,3,3],[3,3,0,2],[1,3,2,2]]

# size = list(map(int,lines[0].split(' ')))
#
# down = []
# for i in range(1,size[0]+1):
# 	down.append(list(map(int,lines[i].split(' '))))
#
# right = []
# for i in range(size[0]+2,2*size[0]+3):
# 	right.append(list(map(int,lines[i].split(' '))))

# print(size)
# print(down)
# print(right)

# print(Manhattan(size,down,right)[size[0]][size[1]])

v='AACCTTGG'
w='ACACTGTGA'

backtrack=LGSBackTrack(v,w)

print(backtrack)
print(OutputLGS(backtrack,v,len(v),len(w)))
