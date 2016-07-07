# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from PatternCount import PatternCount
from FrequentWords import FrequentWords
from ComputingFrequencies import ComputingFrequencies
from ComputingFrequencies import PatternToNumber
from ComputingFrequencies import NumberToPattern
from ReverseSequence import ReverseSequence
from PatternMatch import PatternMatch
from ClumpFinding import ClumpFinding

# import sys # you must import "sys" to read from STDIN
# lines = sys.stdin.read().splitlines() # read in the input from STDIN

# for i in range(len(lines)):
# 	print('Line ' + str(i+1) + ' is ' + str(len(lines[i])) + ' characters long.')
#

# print(lines[0])
# print(lines[1])
# print(type(lines[1]))
# print(int(lines[1]))

#print(FrequentWords(lines[0],int(lines[1])))

# result = ComputingFrequencies(lines[0],int(lines[1]))
# print(' '.join(map(str,result)))

# print(ComputingFrequencies('ACGCGGCTCTGAAA',2))
# print(PatternToNumber('CCAGACCGTCGTTGAGGTA'))
#
# print(NumberToPattern(5505,11))
# print(lines[0])
# print(ReverseSequence(lines[0]))


# result = PatternMatch('CTTGATCAT',lines[0])
# print(' '.join(map(str,result)))

# Genome = lines[0]
# [k,L,t] = lines[1].split()
# print(Genome)
# print(k)
# print(L)
# print(t)

#
# Genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
# k = 5
# L = 50
# t = 4
#
# Genome = lines[0]
# k=9
# L=500
# t=3
# result = ClumpFinding(Genome,int(k),int(t),int(L))
# print(' '.join(map(str,result)))
# print(len(result))
# print(PatternCount(Genome,'AAAAAAAGCAG'))

print(PatternCount('CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC','CGCG'))
print(FrequentWords('CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT',3))
print(ReverseSequence('GCTAGCT'))