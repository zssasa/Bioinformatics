# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from StringComposition import StringComposition
from GenomePathString import GenomePathString
from OverlapGraph import OverlapGraph
from DeBrujin import DeBrujinFromText
from DeBrujin import DeBrujinFromKmers

import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

# result = StringComposition(int(lines[0]),lines[1])
# for kmer in result:
# 	print(kmer)

# GenomePathString(lines)
# print(GenomePathString(lines))


# result = OverlapGraph(lines)
# for edge in  result:
# 	print(" -> ".join(edge))

# result = DeBrujin(4,'AAGATTCTCTAAGA')
# result = DeBrujinFromText(int(lines[0]),lines[1])
# # print(type(result))
# result = sorted(result.items(), key=lambda d:d[0])
# # print(type(result))
# # print(result)
# for a in  result:
# 	print('%s -> %s' %(a[0],','.join(a[1])))
# for key in result:
# 	print('%s -> %s' %(key,result[key]))

result = DeBrujinFromKmers(lines)
result = sorted(result.items(), key=lambda d:d[0])
for a in result:
	print('%s -> %s' %(a[0],','.join(a[1])))