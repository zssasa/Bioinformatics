# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from CyclopeptideScoringWithMass import LeaderboardCyclopeptideSequencing

def SpectralConvolution(spectrum):
	result = []
	spectrum = sorted(spectrum)
	for i in range(len(spectrum)-1):
		for j in range(i+1,len(spectrum)):
			if spectrum[j]-spectrum[i] > 0:
				result.append(spectrum[j]-spectrum[i])
	return result

def ConvolutionCyclopeptideSequencing(M, N, spectrum):
	spectrum = sorted(spectrum)
	convolution_spectrum = SpectralConvolution(spectrum)
	peptide_alphabet = {}
	peptide_mass = []
	for key in set(convolution_spectrum):
		if key>=57 and key<=200:
			peptide_alphabet[key] = peptide_alphabet.setdefault(key,0) + 1
	peptide_frequency = sorted(peptide_alphabet.values(),reverse=True)
	M_frequency = peptide_frequency[M-1]
	for key in peptide_alphabet:
		if peptide_alphabet[key] >= M_frequency:
			peptide_mass.append(key)
	peptide_mass = sorted(peptide_mass)
	# print(peptide_mass)
	result = LeaderboardCyclopeptideSequencing(spectrum,N,peptide_mass)
	return result




if __name__ == '__main__':
	# with open('./data/spectral_convolution_test.txt') as f:
	# 	spectrum = list(map(int,f.readline().strip().split()))
	# spectrum = [0, 137, 186, 323]
	# s = SpectralConvolution(spectrum)
	# print(len(s))
	# print(' '.join(map(str,s)))

	# with open('./data/convolution_cyclopeptide_sequencing_test.txt') as f:
	# 	M = int(f.readline().strip())
	# 	N = int(f.readline().strip())
	# 	spectrum = list(map(int,f.readline().strip().split()))
	# M = 20
	# N = 60
	# spectrum = [57, 57, 71, 99, 129, 137, 170, 186, 194, 208, 228, 265, 285, 299, 307, 323, 356, 364, 394, 422, 493]
	# s = ConvolutionCyclopeptideSequencing(M,N,spectrum)
	# print('-'.join(map(str,s[0])))
	# s_len = [len(ss) for ss in s]
	# s_minlen = min(s_len)
	# for ss in s:
	# 	if len(ss) == s_minlen:
	# 		print(ss)
	# 		break
	with open('Tyrocidine_B1_Spectrum_25.txt') as f:
		spectrum = list(map(int,f.readline().strip().split()))
	N = 1000
	M = 20
	s = ConvolutionCyclopeptideSequencing(M,N,spectrum)
	for ss in s:
		print('-'.join(map(str,ss)))
	print(len(s))