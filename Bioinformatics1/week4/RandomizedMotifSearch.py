# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

import random
from operator import ne


# def hamming_distance(str1, str2):
# 	assert len(str1) == len(str2)
# 	dist = 0
# 	for i in range(len(str1)):
# 		if str1[i] != str2[i]:
# 			dist += 1
# 	return dist

# def MotifScore(Motifs):
# 	consensus = [0 for i in range(len(Motifs[0]))]
# 	dist = 0
# 	for i in range(len(Motifs[0])):
# 		col = [motif[i] for motif in Motifs]
# 		items = dict((col.count(i),i) for i in col)
# 		consensus[i] = items[max(list(items.keys()))]
# 	consensus = ''.join(consensus)
# 	# print(consensus)
# 	for motif in Motifs:
# 		dist += hamming_distance(consensus,motif)
# 	return dist

def hamming_distance(seq1, seq2):
    'Returns the Hamming distance between equal-length sequences.'
    if len(seq1) != len(seq2):
        raise ValueError('Undefined for sequences of unequal length.')
    return sum(map(ne, seq1, seq2))


def MotifScore(motifs):
    '''Returns the score of the dna list motifs.'''
    # print(motifs)
    score = 0
    for i in range(len(motifs[0])):
        motif = ''.join([motifs[j][i] for j in range(len(motifs))])
        score += min([hamming_distance(motif, homogeneous * len(motif)) for homogeneous in 'ACGT'])
    return score


def ProfileFromMotifsLaplace1(motifs):
    '''Returns the profile of the dna list motifs.'''
    prof = []
    for i in range(len(motifs[0])):
        col = ''.join([motifs[j][i] for j in range(len(motifs))])
        prof.append([float(col.count(nuc) + 1) / float(len(col) + 4) for nuc in 'ACGT'])
    return prof


def ProfileFromMotifsLaplace(Motifs):
    # profile = dict()
    profile = [[0 for _ in range(len(Motifs[0]))] for _ in range(4)]
    for i in range(len(Motifs[0])):
        col = [motif[i] for motif in Motifs]
        profile[0][i] = (col.count('A') + 1) / (len(col) + 4)
        profile[1][i] = (col.count('C') + 1) / (len(col) + 4)
        profile[2][i] = (col.count('G') + 1) / (len(col) + 4)
        profile[3][i] = (col.count('T') + 1) / (len(col) + 4)
    return profile


def MostProbableKmer(text, k, profile):
    nuc_loc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}
    maxProb = 0
    index = 0
    for i in range(len(text) - k + 1):
        prob = 1
        for j in range(k):
            prob *= profile[nuc_loc[text[i + j]]][j]
            # if text[i + j] == 'A':
            #     prob *= profile[0][j]
            # elif text[i + j] == 'C':
            #     prob *= profile[1][j]
            # elif text[i + j] == 'G':
            #     prob *= profile[2][j]
            # elif text[i + j] == 'T':
            #     prob *= profile[3][j]
        if prob > maxProb:
            maxProb = prob
            index = i
    return text[index:index + k]


def RandomizedMotifSearch(texts, k, t):
    # random_motifs = []
    # for i in range(t):
    # 	tem = random.randint(0,len(texts[i])-k)
    # 	random_motifs.append(texts[i][tem:tem+k])
    random_pos = [random.randint(0, len(texts[i]) - k) for i in range(t)]
    motifs = [texts[i][r:r + k] for i, r in enumerate(random_pos)]
    # random_motifs = [text[pos:pos + k] for text, pos in zip(texts, random_pos)]
    # random_motifs = [text[random.randint(0,len(text)-k+1)] for text in texts]
    # print(random_motifs)
    best_motifs = motifs
    while True:
        profile = ProfileFromMotifsLaplace(motifs)
        motifs = [MostProbableKmer(text, k, profile) for text in texts]
        if MotifScore(motifs) < MotifScore(best_motifs):
            best_motifs = motifs
        else:
            return MotifScore(best_motifs), best_motifs


def RepeatRandomized(texts, k, t, iter_num=1000):
    best_score, best_motifs = RandomizedMotifSearch(texts, k, t)
    for _ in range(iter_num):
        score, motifs = RandomizedMotifSearch(texts, k, t)
        if MotifScore(motifs) < MotifScore(best_motifs):
            best_motifs = motifs
        # best_score = score
    return MotifScore(best_motifs), best_motifs


def ProfileRandomlyGeneratedKmer(text, profile):
    m = len(profile[0])
    nuc_loc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}
    distribution = [1 for _ in range(len(text)-m+1)]
    for i in range(len(text)-m+1):
        for j in  range(m):
            distribution[i] *= profile[nuc_loc[text[i+j]]][j]
    total = sum(distribution)
    distribution_norm = [prob/total for prob in distribution]
    index = 0
    tem = random.random()
    for i in range(len(text)-m+1):
        if tem <= sum(distribution_norm[:i+1]):
            index = i
            break
    return text[index:index+m]


def GibbsSampler(texts, k, t, iter_num=1000):
    random_pos = [random.randint(0, len(texts[i]) - k) for i in range(t)]
    motifs = [texts[i][r:r + k] for i, r in enumerate(random_pos)]
    best_motifs = motifs
    for j in range(iter_num):
        i = random.randint(0, t - 1)
        # print(i)
        # print(motifs[i])
        current_profile = ProfileFromMotifsLaplace([motif for index, motif in enumerate(motifs) if index!=i])
        # profile = ProfileFromMotifsLaplace(motifs[:i]+motifs[i+1:])
        motifs = [ProfileRandomlyGeneratedKmer(texts[i],current_profile) if index == i else motif for index, motif in
                  enumerate(motifs)]
        # print(motifs[i])
        current_score = MotifScore(motifs)
        if current_score < MotifScore(best_motifs):
            best_motifs = motifs
    return MotifScore(best_motifs), best_motifs


if __name__ == '__main__':
    # with open('./data/randomized_motif_search_test.txt') as f:
    #     k, t = list(map(int, f.readline().strip().split()))
    #     texts = f.readlines()
    # texts = [text.strip() for text in texts]
    # print(k)
    # print(t)
    # print(len(texts))
    # print(len(texts[0]))
    # k = 8
    # t = 5
    # N = 100
    # texts = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
    # 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
    # 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
    # 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
    # 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    # print(RandomizedMotifSearch(texts,k,t))
    # for i in range(2):
    # s = RepeatRandomized(texts, k, t, 1000)
    # print('\n'.join(s[1]))

    with open('./data/gibbs_test.txt') as f:
        k,t,N = list(map(int,f.readline().strip().split()))
        texts = f.readlines()
    texts = [text.strip() for text in texts]
    # print(k)
    # print(t)
    # print(N)
    for i in range(20):
        s = GibbsSampler(texts,k,t,N)
        print(s)
    # print('\n'.join(s[1]))

    # with open('score.txt') as f:
    #     motifs = f.readlines()
    # motifs = [motif.strip() for motif in motifs]
    # motifs=['TCTCGGGG','CCAAGGTG','TACAGGCG','TTCAGGTG','TCCACGTG']
    # print(MotifScore(motifs))
    # print(ProfileFromMotifsLaplace(motifs))
    # print(ProfileFromMotifsLaplace1(motifs))
