# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import  pprint
from collections import defaultdict


def LoadAminoMassAcid():
	AAmass = dict()

	with open('integer_mass_table1.txt') as f:
		for line in f:
			line = line.split()
			if line[1] not in AAmass:
				AAmass[int(line[1])] = line[0]
	# print(AAmass)
	return AAmass

def LoadAminoAcidMass():
	AAmass = dict()

	with open('integer_mass_table1.txt') as f:
		for line in f:
			line = line.split()
			if line[0] not in AAmass:
				AAmass[line[0]] = int(line[1])
	# print(AAmass)
	return AAmass

def SpectrumGraph(spectrum):
	AAmass = LoadAminoMassAcid()
	# spectrum.append(0)
	spectrum = sorted(spectrum)

	# print(spectrum)
	result = dict()

	for i in range(len(spectrum)-1):
		for j in range(i+1,len(spectrum)):
			tem = spectrum[j]-spectrum[i]
			if tem in AAmass:
				# result[(i,j)] = AAmass[tem]
				result[(spectrum[i],spectrum[j])] = AAmass[tem]
	return result


def Mass(peptide):
	AAmass = LoadAminoAcidMass()
	if peptide == []:
		return 0
	mass = 0
	for i in range(len(peptide)):
		mass += AAmass[peptide[i]]
	return mass


def IdealSpectrum(peptide):
	spectrum = []
	for i in range(len(peptide)):
		spectrum.append(Mass(peptide[:i]))
		spectrum.append(Mass(peptide[i:]))
	spectrum = sorted(spectrum)
	return spectrum

def Graph2Edges(graph):
	edges = dict()
	graph_edges = graph.keys()
	for edge in graph_edges:
		edges.setdefault(edge[0],[]).append(edge[1])
	return edges


def DecodingIdealSpectrum(spectrum):
	AAmass = LoadAminoMassAcid()
	spectrum.append(0)
	spectrum = sorted(spectrum)
	spectrum_graph = SpectrumGraph(spectrum)
	# print(spectrum_graph)
	spectrum_edges = Graph2Edges(spectrum_graph)
	# print(spectrum_edges)
	def dfs_path(start, goal):
		stack = [(start, [start])]
		while stack:
			(vertex, path) = stack.pop()
			for next in set(spectrum_edges[vertex]) - set(path):
				# print(next)
				if next == goal:
					yield path+[next]
				else:
					# print(stack)
					stack.append((next,path+[next]))
					# print(stack)
	def path_to_peptide(path):
		peptide = ""
		for i in range(len(path)-1):
			peptide += AAmass[path[i+1]-path[i]]
		return peptide
	sink_to_source = list(dfs_path(0,max(spectrum)))
	# print(sink_to_source)
	# print(sink_to_source)
	result = []
	for path in sink_to_source:
		peptide = path_to_peptide(path)
		# print(peptide)
		# print(IdealSpectrum(peptide))
		if IdealSpectrum(peptide) == spectrum:
			result.append(peptide)
	return result


def PeptideVector(peptide):
	AAmass = LoadAminoAcidMass()
	peptide_mass = [AAmass[p] for p in peptide]
	prefix_mass = []
	for i in range(len(peptide)):
		prefix_mass.append(sum(peptide_mass[:i+1]))
	# print(prefix_mass)
	max_mass = max(prefix_mass)
	# print(max_mass)

	peptide_vector = [0 for _ in range(max_mass)]
	# print(peptide_vector)
	for mass in prefix_mass:
		# print(mass)
		peptide_vector[mass-1] = 1
	return peptide_vector

def Vector2Peptide(peptide_vector):
	# spectrum = [0]
	spectrum = []
	for i in range(len(peptide_vector)):
		if peptide_vector[i] == 1:
			spectrum.append(i+1)
	# print(spectrum)
	peptide = DecodingBinarySpectrum(spectrum)
	return peptide

def DecodingBinarySpectrum(spectrum):
	AAmass = LoadAminoMassAcid()
	spectrum.append(0)
	spectrum = sorted(spectrum)
	spectrum_graph = SpectrumGraph(spectrum)
	# print(spectrum_graph)
	spectrum_edges = Graph2Edges(spectrum_graph)
	# print(spectrum_edges)
	def dfs_path(start, goal):
		stack = [(start, [start])]
		while stack:
			(vertex, path) = stack.pop()
			for next in set(spectrum_edges[vertex]) - set(path):
				# print(next)
				if next == goal:
					yield path+[next]
				else:
					# print(stack)
					stack.append((next,path+[next]))
					# print(stack)
	def path_to_peptide(path):
		peptide = ""
		for i in range(len(path)-1):
			peptide += AAmass[path[i+1]-path[i]]
		return peptide
	def PrefixMass(peptide):
		AAmass = LoadAminoAcidMass()
		peptide_mass = [AAmass[p] for p in peptide]
		prefix_mass = [0]
		for i in range(len(peptide)):
			prefix_mass.append(sum(peptide_mass[:i+1]))
		return prefix_mass
	sink_to_source = list(dfs_path(0,max(spectrum)))
	# print(sink_to_source)
	# print(sink_to_source)
	result = []
	for path in sink_to_source:
		peptide = path_to_peptide(path)
		# print(peptide)
		# print(IdealSpectrum(peptide))
		if PrefixMass(peptide) == spectrum:
			result.append(peptide)
	return result



def PeptideSequencing(spectrum):
	AAmass = LoadAminoMassAcid()
	spectrum.insert(0,0)
	source = 0
	sink = len(spectrum) - 1
	# print(spectrum)
	# print(len(spectrum))
	def Spectrum2DAG(spectrum):
		result = dict()
		for i in range(len(spectrum)-1):
			for j in range(i+1,len(spectrum)):
				tem = j-i
				if tem in AAmass:
					result[(i,j)] = AAmass[tem]
		return result
	def Graph2Edges(graph):
		edges = dict()
		graph_edges = graph.keys()
		for edge in graph_edges:
			edges.setdefault(edge[0],[]).append(edge[1])
		return edges
	spectrum_graph = Spectrum2DAG(spectrum)
	# print(spectrum_graph)
	# print(len(spectrum_graph))

	spectrum_edges = Graph2Edges(spectrum_graph)
	# print(spectrum_edges)

	spectrum_new_graph = dict()
	for key in spectrum_graph:
		spectrum_new_graph[key] = spectrum[key[1]]
	# print(spectrum_new_graph[(581, 638)])


	# incomings = {edge[0] for edge in spectrum_graph.keys()}-{edge[1] for edge in spectrum_graph.keys()}
	# print(incomings)
	# for incoming in incomings:
	# 	for key in list(spectrum_graph.keys()):
	# 		if incoming == key[0]:
	# 			del spectrum_graph[key]
	# incomings = {edge[0] for edge in spectrum_graph.keys()}-{edge[1] for edge in spectrum_graph.keys()}
	# print(incomings)
	# s = [ -float("inf") for _ in range(sink-source+1)]
	# source = 1
	s = {node:-float("inf") for node in {edge[0] for edge in spectrum_graph.keys()}
		 | {edge[1] for edge in spectrum_graph.keys()}}
	s[source] = 0
	backtrack = {node:None for node in range(1,sink-source+1)}
	for i in range(1,sink-source+1):
		try:
			s[i], backtrack[i] = max(map(lambda e: [s[e[0]] + spectrum[i], e[0]],
											   filter(lambda e: e[1] == i, spectrum_graph.keys())), key=lambda p:p[0])
		except ValueError:
			pass
	# print(s)
	path = [sink]
	while path[0] != source:
		path = [backtrack[path[0]]] + path
	# print(path)
	# print(s[sink])
	peptide = ""
	for i in range(1,len(path)):
		peptide += AAmass[path[i]-path[i-1]]
	# print(peptide)
	return s[sink], peptide




if __name__ == '__main__':
	# with open('./data/spectrum_graph_test.txt') as f:
	# 	spectrum = list(map(int,f.readline().strip().split()))
	# spectrum = [57, 71, 154, 185, 301, 332, 415, 429, 486]
	# s = SpectrumGraph(spectrum)
	# pprint(s)
	# s_key = s.keys()
	# s_key = sorted(s_key,key=lambda d:(d[0], d[1]))
	# print(s_key)
	# for ss in s_key:
	# 	print('%d->%d:%s' %(ss[0],ss[1],s[ss]))
	# peptide = 'GPG'
	# print(IdealSpectrum(peptide))
	# print(IdealSpectrum('GPFNA'))
	# print(DecodingIdealSpectrum(spectrum))

	# with open('./data/decoding_ideal_spectrum_test.txt') as f:
	# 	spectrum = list(map(int,f.readline().strip().split()))
	# print(DecodingIdealSpectrum(spectrum)[0])


	# with open('./data/peptide_to_peptide_vector_test.txt') as f:
	# 	peptide = f.readline().strip()
	# peptide = 'XZZXX'
	# s = PeptideVector(peptide)
	# print(' '.join(map(str,s)))

	# with open('./data/peptide_vector_to_peptide_test.txt') as f:
	# 	peptide_vector = list(map(int,f.readline().strip().split()))
	# peptide_vector = [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
	# print(Vector2Peptide(peptide_vector)[0])
	# print(IdealSpectrum('FRVLRCLEDQPLGLMAQPHRTMPDHPQFTGDAHHMYATC'))

	with open('./data/peptide_sequencing_test.txt') as f:
		spectrum = list(map(int,f.readline().strip().split()))
	# spectrum = [0, 0, 0, 4, -2, -3, -1, -7, 6, 5, 3, 2, 1, 9, 3, -8, 0, 3, 1, 2, 1, 8]
	print(PeptideSequencing(spectrum))