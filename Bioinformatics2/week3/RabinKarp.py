# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint



nucleotide = {'A':1,'C':2,'G':3,'T':4}

def RNAtoDNA(RNA):
	DNA = RNA.replace('U','T')
	return DNA

def ProteinToDNA(protein):
	protein_table = dict()
	with open('RNA_codon_table_1.txt') as f:
		for line in f:
			line = line.split()
			if len(line) > 1:
				if line[1] in protein_table:
					protein_table[line[1]].append(line[0])
				else:
					protein_table[line[1]] = [line[0]]
			else:
				if 'STP' in protein_table:
					protein_table['STP'].append(line[0])
				else:
					protein_table['STP'] = [line[0]]
	# print(len(protein_table))
	# pprint(protein_table)
	RNA1 = ['']
	RNA2 = []
	for i in range(len(protein)):
		s = protein_table[protein[i]]
		# print(s)
		# print(len(s))
		for t in RNA1:
			for ss in s:
				# print(ss)
				RNA2.append(t+ss)
			# DNA.remove(t)
		RNA1 = RNA2
		RNA2 = []
	DNA = [RNAtoDNA(RNA) for RNA in RNA1]
	return DNA



def RabinKarp(str1, str2, q, d):
	count = 0
	n = len(str1)
	m = len(str2)
	if n<m:
		return count
	i = 1
	h = 1
	for i in range(1,m):
		h = h*d%q
	p = 0
	t = 0
	for i in range(m):
		p = (( d*p + nucleotide[str2[i]]) % q)
		t = (( d*t + nucleotide[str1[i]]) % q)
	# s = 0
	for s in range(n-m+1):
		if p == t:
			for i in range(m):
				if str2[i] != str1[s+i]:
					break
			if i==m:
				# print('pattern occurs with shift %d' %s)
				count += 1
		if s<n-m:
			t= (  d* (t - nucleotide[str1[s]]*h%q + q) + nucleotide[str1[s+m]])  % q
	# print('string matching ends')
	return count

def RabinKarp_multiple(str1, str2s, q, d):
	count = 0
	n = len(str1)
	m = len(str2s[0])
	i = 1
	h = 1
	for i in range(1,m):
		h = h*d%q
	p = [0 for i in range(len(str2s))]
	t = 0
	for i in range(m):
		for j in range(len(str2s)):
			p[j] = (( d*p[j] + nucleotide[str2s[j][i]]) % q)
		t = (( d*t + nucleotide[str1[i]]) % q)
	for s in range(n-m+1):
		if s == int((n-m)/10):
			print('10% is closed')
		elif s == int((n-m)/5):
			print('20% is closed')
		elif s == int((n-m)/3):
			print('30% is closed')
		elif s == int((n-m)/2):
			print('50% is closed')
		elif s == int((n-m)*3/5):
			print('60% is closed')
		elif s == int((n-m)*4/5):
			print('80% is closed')
		elif s == int((n-m)*9/10):
			print('90% is closed')

		for j in range(len(str2s)):
			if p[j] == t:
				for i in range(m):
					if str2s[j][i] != str1[s+i]:
						break
				if i==m:
					count += 1
		if s<n-m:
			t= (  d* (t - nucleotide[str1[s]]*h%q + q) + nucleotide[str1[s+m]])  % q
	return count




if __name__ == '__main__':
	# with open('Bacillus_brevis.txt') as f:
	# 	DNA = f.readlines()
	# DNA = [line.strip() for line in DNA]
	# DNA = ''.join(DNA)
	protein = 'LEADER'
	s = ProteinToDNA(protein)
	print(len(s))
	# print(RabinKarp_multiple(DNA,s,6999997,4))
	# print(len(ProteinToDNA(protein)))
	# count = 0
	# for ss in s:
	# 	count += RabinKarp(DNA,ss,6999997,4)
	# print(count)

