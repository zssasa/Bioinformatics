# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


from TheoreticalSpectrum import LoadAminoAcidMass
from TheoreticalSpectrum import CyclicSpectrum
from TheoreticalSpectrum import LinearSpectrum
PeptideMass = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def CyclopeptideSequencing(spectrum):
	AAmass = LoadAminoAcidMass()
	def Mass(peptide):
		mass = 0
		for i in range(len(peptide)):
			mass += AAmass[peptide[i]]
		return mass
	def Expand(peptides):
		new_peptides = []
		for peptide in peptides:
			for key in AAmass:
				new_peptides.append(peptide+key)
		return new_peptides
	def Consistent(peptide):
		linear_spectrum = LinearSpectrum(peptide,AAmass)
		# if peptide=='C':
		# 	print(linear_spectrum)
		for s in linear_spectrum:
			if linear_spectrum.count(s) > spectrum.count(s):
				return False
		return True
	def PeptidesToStr(peptides_):
		str_ = []
		for peptide_ in peptides_:
			s_ = []
			for i in range(len(peptide_)):
				s_.append(AAmass[peptide_[i]])
			if s_ not in str_:
				str_.append(s_)
		# str = [set(a) for a in str]
		# print(str)
		# str = set(str)
		return str_

	print(Consistent('TCE'))
	print(Consistent('TCQ'))
	print(Consistent('VAQ'))
	print(Consistent('AQV'))
	print(Consistent('QCV'))
	print(Consistent('CTV'))
	# print(Consistent('TCE'))

	# print(LinearSpectrum('HAMNL',AAmass))
	result = []
	peptides = ['']
	# tem = []
	while peptides:
		peptides = Expand(peptides)
		# print(peptides)
		# peptides = tem
		tem = []
		# print(sorted(tem))
		# print(sorted(peptides))
		for i in range(len(peptides)):
			peptide = peptides[i]
		# for peptide in tem:
		# 	print(peptide)
			if Mass(peptide) == max(spectrum):
				# print(peptide)
				if CyclicSpectrum(peptide,AAmass) == spectrum:
					result.append(peptide)
					tem.append(peptide)
					# peptides.remove(peptide)
			elif not Consistent(peptide):
				tem.append(peptide)
				# print(peptide)
				# peptides.remove(peptide)
		for i in range(len(tem)):
			peptides.remove(tem[i])
		# print(sorted(peptides))
		# break
	# print(result)
	# result = PeptidesToStr(result)
	return result



if __name__ == '__main__':
	# with open('./data/cyclopeptide_sequencing_test.txt') as f:
	# 	spectrum = list(map(int,f.readline().split()))
	# print(spectrum)
	# spectrum = [0, 71, 101, 113, 131, 184, 202, 214, 232, 285, 303, 315, 345, 416]
	spectrum = [0, 71, 99, 101, 103, 128, 129, 199, 200, 204, 227, 230, 231, 298, 303, 328, 330, 332, 333]
	# print(CyclopeptideSequencing)
	s = CyclopeptideSequencing(spectrum)
	# for ss in s:
	# 	print(ss)
	# 	print('-'.join(map(str,ss)),end=' ')
	# print(len(CyclopeptideSequencing(spectrum)))

