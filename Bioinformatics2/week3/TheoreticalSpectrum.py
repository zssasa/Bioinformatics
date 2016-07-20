# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


def LoadAminoAcidMass():
	AAmass = dict()
	with open('integer_mass_table.txt') as f:
		for line in f:
			line = line.split()
			if line[0] not in AAmass:
				AAmass[line[0]] = int(line[1])
	return AAmass


def LinearSpectrum(peptide,AAmass):
	PrefixMass = [0 for i in range(len(peptide)+1)]
	for i in range(len(peptide)):
		PrefixMass[i+1] = PrefixMass[i] + AAmass[peptide[i]]

	Linear_Spectrum = []
	for i in range(len(peptide)):
		for j in range(i+1,len(peptide)+1):
			Linear_Spectrum.append(PrefixMass[j]-PrefixMass[i])
	Linear_Spectrum.append(0)
	LinearSpectrum = sorted(Linear_Spectrum)
	return LinearSpectrum

def CyclicSpectrum(peptide,AAmass):
	PrefixMass = [0 for i in range(len(peptide)+1)]
	for i in range(len(peptide)):
		PrefixMass[i+1] = PrefixMass[i] + AAmass[peptide[i]]

	peptideMass = PrefixMass[len(peptide)]

	Cyclic_Spectrum = []
	for i in range(len(peptide)):
		for j in range(i+1,len(peptide)+1):
			Cyclic_Spectrum.append(PrefixMass[j]-PrefixMass[i])
			if i>0 and j<len(peptide):
				Cyclic_Spectrum.append(peptideMass-(PrefixMass[j]-PrefixMass[i]))
	Cyclic_Spectrum.append(0)
	Cyclic_Spectrum = sorted(Cyclic_Spectrum)
	return Cyclic_Spectrum

if __name__ == '__main__':
	# with open('./data/LinearSpectrum_test.txt') as f:
	with open('./data/CyclicSpectrum_test.txt') as f:
		peptide = f.readline().strip()
	AAmass = LoadAminoAcidMass()
	peptide = 'TMLA'
	# print(' '.join(map(str,LinearSpectrum(peptide,AAmass))))
	print(' '.join(map(str,CyclicSpectrum(peptide,AAmass))))