# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

# from ProteinTranslate import LoadRNACodon
from ProteinTranslate import ProteinTranslation

ReverseDict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}


def ReverseSequence(Sequence):
	result = ""
	for i in range(len(Sequence)-1,-1,-1):
		# print(i)
		result += ReverseDict[Sequence[i]]
	return result


def DNAtoRNA(DNA):
	RNA = DNA.replace('T','U')
	return RNA


def PeptideEncoding(DNA, peptide):
	sequence = []
	protein_length = len(peptide)
	for i in range(len(DNA)-3*protein_length+1):
		if ProteinTranslation(DNAtoRNA(DNA[i:i+protein_length*3])) == peptide \
				or ProteinTranslation(DNAtoRNA(ReverseSequence(DNA[i:i+protein_length*3]))) == peptide:
			sequence.append(DNA[i:i+protein_length*3])
	return sequence

if __name__ == '__main__':
	with open('./data/PeptideEncoding_test.txt') as f:
		DNA = f.readline().strip()
		peptide = f.readline().strip()
	# DNA = 'ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
	# peptide = 'MA'
	# with open('Bacillus_brevis.txt') as f:
	# 	DNA = f.readlines()
	# DNA = [line.strip() for line in DNA]
	# DNA = ''.join(DNA)
	# peptide = 'VKLFPWFNQY'
	seq = PeptideEncoding(DNA,peptide)
	for s in seq:
		print(s)
	# print(len(seq))