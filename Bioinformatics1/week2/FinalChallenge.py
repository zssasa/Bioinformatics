# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from Skew import minSkew
from FrequentWordsWithMismatches import FrequentWordsWithMismatchesAndReverseComplements

genome = ""
with open('./data/Salmonella_enterica.txt') as f:
	f.readline()
	for line in f.readlines():
		genome += line.strip()

# print(genome)e
# print(minSkew(genome))
pos = [3764856, 3764858]
localGenome = genome[pos[0]-500: pos[1]+500]
print(localGenome)

print(FrequentWordsWithMismatchesAndReverseComplements(localGenome, 9, 1))
