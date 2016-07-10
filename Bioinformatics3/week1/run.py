# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from DPChange import DPChange
from Manhattan import Manhattan
from LCS import LCSBackTrack
#from LCS import OutputLCS
from LCS import OutputLCS2
from LongestPathDAG import ParseEdge
from LongestPathDAG import Graph
from LongestPathDAG import TopologicalSort
from LongestPathDAG import LongestPathDAG
from pprint import pprint

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

v='AGACTG'
w='GTACGA'

# v=lines[0]
# w=lines[1]
#
backtrack=LCSBackTrack(v,w)
#
# # print(backtrack)
s=OutputLCS2(backtrack,v,len(v),len(w))
print(s)

# source = 0
# sink = 4
# lines = ['0->1:7','0->2:4','2->3:2','1->4:1','3->4:3']


# source = int(lines[0])
# sink = int(lines[1])
# edges = lines[2:]
# G = Graph(source,sink,edges)
# pprint(G)
# print(G[4])
# print(G[4] in G)
# G_sorted = TopologicalSort(G)
# pprint(G_sorted)
# s = LongestPathDAG(source,sink,G_sorted)
# print(s)
