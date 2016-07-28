# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

# PeptideMass = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
# PeptideMass = list(range(57,201))
import copy

def LoadAminoAcidMass():
	AAmass = dict()
	with open('integer_mass_table.txt') as f:
		for line in f:
			line = line.split()
			if line[0] not in AAmass:
				AAmass[line[0]] = int(line[1])
	# print(AAmass)
	return AAmass

def LinearSpectrum(peptide):
	PrefixMass = [0 for i in range(len(peptide)+1)]
	for i in range(len(peptide)):
		PrefixMass[i+1] = PrefixMass[i] + peptide[i]

	Linear_Spectrum = []
	for i in range(len(peptide)):
		for j in range(i+1,len(peptide)+1):
			Linear_Spectrum.append(PrefixMass[j]-PrefixMass[i])
	Linear_Spectrum.append(0)
	LinearSpectrum = sorted(Linear_Spectrum)
	return LinearSpectrum

def CyclicSpectrum(peptide):
	PrefixMass = [0 for _ in range(len(peptide)+1)]
	for i in range(len(peptide)):
		PrefixMass[i+1] = PrefixMass[i] +peptide[i]

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


def CyclopeptideScoring(peptide, spectrum):
	if peptide == []:
		return 0
	# AAmass = LoadAminoAcidMass()
	spectrum_dict = dict()
	for key in spectrum:
		spectrum_dict[key] = spectrum_dict.setdefault(key,0) + 1
	# print(AAmass)
	cyclic_spectrum = CyclicSpectrum(peptide)

	cyclic_dict = dict()
	for key in cyclic_spectrum:
		cyclic_dict[key] = cyclic_dict.setdefault(key,0) + 1
	score = 0
	for key in cyclic_dict:
		if key in spectrum_dict:
			score += min(cyclic_dict[key],spectrum_dict[key])
	return score


def LinearScoring(peptide,spectrum):
	if peptide == '':
		return 0
	# AAmass = LoadAminoAcidMass()
	spectrum_dict = dict()
	for key in spectrum:
		spectrum_dict[key] = spectrum_dict.setdefault(key,0) + 1
	# print(AAmass)
	linear_spectrum = LinearSpectrum(peptide)

	linear_dict = dict()
	for key in linear_spectrum:
		linear_dict[key] = linear_dict.setdefault(key,0) + 1
	score = 0
	for key in linear_dict:
		if key in spectrum_dict:
			score += min(linear_dict[key],spectrum_dict[key])
	return score

# def Trim(Leaderboard, spectrum, N):
# 	result = []
# 	peptide_score = dict()
# 	for peptide in Leaderboard:
# 		peptide_score[peptide] = LinearScoring(peptide,spectrum)
# 	peptide_sorted_score = sorted(peptide_score.values(),reverse=True)
# 	if len(peptide_sorted_score) < N:
# 		return Leaderboard
# 	NScore = peptide_sorted_score[N-1]
# 	for peptide in peptide_score:
# 		if peptide_score[peptide] >= NScore:
# 			result.append(peptide)
# 	return result

def LeaderboardCyclopeptideSequencing(spectrum, N, PeptideMass):
	# AAmass = LoadAminoAcidMass()
	def Mass(peptide):
		mass = 0
		for i in range(len(peptide)):
			mass += peptide[i]
		return mass
	def Expand(peptides):
		new_peptides = []
		for peptide_ in peptides:
			# tem = peptide_
			# tem = []
			# tem = copy.deepcopy(peptide_)
			for key_ in PeptideMass:
				tem = copy.deepcopy(peptide_)
				# print(key_)
				# print(peptide_)
				tem.append(key_)
				# print(tem)
				# print(tem)
				new_peptides.append(tem)
		return new_peptides

	def Trim(peptides):
		if len(peptides)<=N:
			return peptides
		result = []

		peptide_score = dict()
		score_ = []
		for peptide in peptides:
			score = LinearScoring(peptide,spectrum)
			score_.append(score)
			if score in peptide_score:
				peptide_score[score].append(peptide)
			else:
				peptide_score[score] = [peptide]
			# peptide_score[peptide] = LinearScoring(peptide,spectrum)
		sorted_score = sorted(score_,reverse=True)

		NScore = sorted_score[N-1]
		for score in peptide_score:
			if score >= NScore:
				result.extend(peptide_score[score])
		return result

	LeaderBoard = [[]]

	LeaderPeptide = ''
	result = []
	while LeaderBoard:
		LeaderBoard = Expand(LeaderBoard)
		# print(LeaderBoard)
		# break
		tem = []
		for i in range(len(LeaderBoard)):
			peptide = LeaderBoard[i]
			if Mass(peptide) == max(spectrum):
				# print(peptide)
				# if LinearScoring(peptide,spectrum) > LinearScoring(LeaderPeptide,spectrum):
				if CyclopeptideScoring(peptide,spectrum) > CyclopeptideScoring(LeaderPeptide,spectrum):
					LeaderPeptide = peptide
					result = []
					result.append(peptide)
				elif CyclopeptideScoring(peptide,spectrum) == CyclopeptideScoring(LeaderPeptide,spectrum):
					result.append(peptide)
			elif Mass(peptide) > max(spectrum):
				tem.append(peptide)
		for i in range(len(tem)):
			LeaderBoard.remove(tem[i])
		LeaderBoard = Trim(LeaderBoard)
	# result = LeaderPeptide
	# result = [AAmass[peptide] for peptide in LeaderPeptide]
	# result = PeptidesToStr(LeaderPeptide)
	return result



if __name__ == '__main__':
	# with open('./data/cyclopeptide_scoring_test.txt') as f:
	# 	peptide = f.readline().strip()
	# 	line = list(map(int,f.readline().strip().split()))
	# spectrum = dict()
	# for key in line:
	# 	spectrum[key] = spectrum.setdefault(key,0) + 1
	# peptide = 'NQEL'
	# spectrum = {0:1, 99:1, 113:1, 114:1, 128:1,
	# 			227:1, 257:1, 299:1, 355:1, 356:1, 370:1, 371:1, 484:1}
	# print(CyclopeptideScoring(peptide,spectrum))
	# print(LinearScoring(peptide,spectrum))
	# with open('./data/Leader_test.txt') as f:
	# 	N = int(f.readline().strip())
	# 	spectrum = list(map(int,f.readline().strip().split()))
	# N = 10
	# spectrum = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]

	with open('Tyrocidine_B1_Spectrum_10.txt') as f:
		spectrum = list(map(int,f.readline().strip().split()))
	N = 1000
	s = LeaderboardCyclopeptideSequencing(spectrum,N)
	print(s)
	print(len(s))
	# print(LinearScoring(s,spectrum))
	# print(CyclopeptideScoring(s,spectrum))

	# print('-'.join(map(str,s)))


	# with open('./data/LinearScore_test.txt') as f:
	# 	peptide = f.readline().strip()
	# 	spectrum = list(map(int,f.readline().strip().split()))
	# peptide = 'VYKGGFWPFIGA'
	# peptide = 'VKLFPWFNQY'
	# print(LinearScoring(peptide,spectrum))
	# print(CyclopeptideScoring(peptide,spectrum))

	# with open('./data/Trim_test.txt') as f:
	# 	leader_board = f.readline().strip().split()
	# 	spectrum = list(map(int,f.readline().strip().split()))
	# 	N = int(f.readline().strip())
	# leader_board = ['LAST', 'ALST', 'TLLT', 'TQAS']
	# spectrum = [0, 71, 87, 101, 113, 158, 184, 188, 259, 271, 372]
	# N = 2
	# s = Trim(leader_board,spectrum,N)
	# print(' '.join(s))
