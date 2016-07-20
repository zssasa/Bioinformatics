# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint


def DNAtoRNA(DNA):
	RNA = DNA.replace('T','U')
	return RNA


def LoadRNACodon():
	RNACodon = dict()
	with open('RNA_codon_table_1.txt') as f:
		for line in f:
			line = line.split()
			# print(line)
			if len(line) > 1:
				RNACodon[line[0]] = line[1]
			else:
				RNACodon[line[0]] = []
			# codon, protein = line.split()
			# RNACodon[codon] = protein
	return RNACodon


def ProteinTranslation(RNA):
	RNACodon = LoadRNACodon()
	protein = ""
	for i in range(0,len(RNA),3):
		if RNACodon[RNA[i:i+3]]:
			protein += RNACodon[RNA[i:i+3]]
		else:
			return protein
	return protein


if __name__ == '__main__':
	with open('./data/protein_translation_test.txt') as f:
		RNA = f.readline().strip()
	# RNAcodon = LoadRNACodon()
	# pprint(RNAcodon)
	# RNA = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
	DNA = 'CCGAGGACCGAAAUCAAC'
	RNA = DNAtoRNA(DNA)

	print(ProteinTranslation(RNA))
		