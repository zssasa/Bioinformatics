# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


from MostProbablekmer import MostProbableKmer
from HammingDistance import hamming_distance


def GreedySearchMotifs(texts, k, t):
	BestMotifs = [text[:k] for text in texts]
	for i in range(len(texts[0])-k+1):
		Motifs = [texts[0][i:i+k]]
		# profile = ProfileFromMotifs(Motifs)
		for j in range(1,t):
			# profile = ProfileFromMotifs(Motifs)
			profile = ProfileFromMotifsLaplace(Motifs)
			motif = MostProbableKmer(texts[j],k,profile)
			Motifs.append(motif)
		if MotifScore(Motifs) < MotifScore(BestMotifs):
			BestMotifs = Motifs
	return BestMotifs


def ProfileFromMotifs(Motifs):
	# m = len(Motifs)
	# n = len(Motifs[0])
	profile = [[0 for i in range(len(Motifs[0]))] for j in range(4)]
	for i in range(len(Motifs[0])):
		col = [motif[i] for motif in Motifs]
		profile[0][i] = col.count('A')/len(col)
		profile[1][i] = col.count('C')/len(col)
		profile[2][i] = col.count('G')/len(col)
		profile[3][i] = col.count('T')/len(col)
	return profile

def ProfileFromMotifsLaplace(Motifs):
	profile = [[0 for i in range(len(Motifs[0]))] for j in range(4)]
	for i in range(len(Motifs[0])):
		col = [motif[i] for motif in Motifs]
		profile[0][i] = (col.count('A')+1)/(len(col)+4)
		profile[1][i] = (col.count('C')+1)/(len(col)+4)
		profile[2][i] = (col.count('G')+1)/(len(col)+4)
		profile[3][i] = (col.count('T')+1)/(len(col)+4)
	return profile


def MotifScore(Motifs):
	consensus = [0 for i in range(len(Motifs[0]))]
	dist = 0
	for i in range(len(Motifs[0])):
		col = [motif[i] for motif in Motifs]
		items = dict((col.count(i),i) for i in col)
		consensus[i] = items[max(list(items.keys()))]
	consensus = ''.join(consensus)
	for motif in Motifs:
		dist += hamming_distance(consensus,motif)
	return dist

if __name__ == '__main__':
	# with open('./data/greedy_motif_search_test.txt') as f:
	with open('./data/GreedyMotifSearchwithPseudocounts_test.txt') as f:
		k,t = list(map(int,f.readline().strip().split()))
		texts = f.readlines()
	# texts = [text.strip() for text in texts]
	# k = 3
	# t = 5
	# texts = ['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG']
	s = GreedySearchMotifs(texts,k,t)
	for ss in s:
		print(ss)
