# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint
from BurrowsWheelerTransformation import BurrowsWheelerTransformation

def BetterBWMatching(FirstOccurrence, LastColumn,Pattern,Count):
	top = 0
	bottom = len(LastColumn) - 1
	while top <= bottom:
		if Pattern:
			# print(Pattern)
			symbol = Pattern[-1]
			# print(symbol)
			Pattern = Pattern[:-1]
			if symbol in LastColumn[top:bottom+1]:
				top = FirstOccurrence[symbol] + Count[symbol][top]
				# print(top)
				bottom = FirstOccurrence[symbol] + Count[symbol][bottom+1] - 1
				# print(bottom)
			else:
				return [0]
		else:
			return top,bottom
			# return bottom - top + 1



def FirstOccurrence(text):
	first_column = sorted(text)
	alphabet = set(text)
	first_occurrence = dict()
	for str in alphabet:
		first_occurrence[str] = first_column.index(str)

	return first_occurrence


def CountRank(text):
	alphabet = set(text)
	count = dict()
	for str in alphabet:
		count[str] = [0 for _ in range(len(text)+1)]
		for i in range(1,len(text)+1):
			if text[i-1] == str:
				count[str][i] = count[str][i-1]+1
			else:
				count[str][i] = count[str][i-1]
	return count

def GetPatternCount(text,patterns):

	first_occurrence = FirstOccurrence(text)
	count = CountRank(text)
	# pprint(count)
	Match_result = [BetterBWMatching(first_occurrence,text,pattern,count) for pattern in patterns]
	result = []
	for ss in Match_result:
		if len(ss)==2:
			result.append(ss[1]-ss[0]+1)
		else:
			result.append(0)
	return result

def SuffixArray(Text):
	suffix = dict()
	for i in range(len(Text)):
		suffix[Text[i:]+Text[:i]] = i
	sorted_suffix = sorted(suffix.items(),key=lambda x:x[0])
	# print(sorted_suffix)
	result = dict()
	for i in range(len(sorted_suffix)):
		result[i] = sorted_suffix[i][1]
	return result

def MultipleMatching(text,patterns):
	bwt = BurrowsWheelerTransformation(text+'$')
	# print(sorted(bwt))
	# print(bwt)
	first_occurrence = FirstOccurrence(bwt)
	# print(first_occurrence)
	count = CountRank(bwt)
	suffix = SuffixArray(text+'$')
	# print(suffix)
	# pprint(count)
	Match_result = [BetterBWMatching(first_occurrence,bwt,pattern,count) for pattern in patterns]
	# print(Match_result)
	result = []
	for ss in Match_result:
		if len(ss) == 1:
			continue
		else:
			for i in range(ss[0],ss[1]+1):
				result.append(suffix[i])
	return result


# def BWMatching(bwt,pattern,firstOccurrence,suffixArray,Count):
# 	top,bottom = BetterBWMatching()

def MultipleApproximatePatternMatching(text,patterns,d):
	bwt = BurrowsWheelerTransformation(text+'$')
	first_occurrence = FirstOccurrence(bwt)
	count = CountRank(bwt)
	suffix = SuffixArray(text+'$')

	# print(bwt)
	# print(first_occurrence)
	# print(count)
	# print(suffix)
	matches = []
	for pattern in patterns:
		seed_locations = seed_detection(bwt, pattern,first_occurrence, suffix,count, d)
		# print(seed_locations)
		seed_match = [seed_index for seed_index in seed_locations if seed_extension(text, pattern, seed_index, d) is True]
		# print(seed_match)
		matches += seed_match
	return matches



def seed_detection(bwt,pattern,firstOccurrence,suffixArray,Count,d):
	k = int(len(pattern)/(d+1))
	seeds = [pattern[i:i+k] for i in range(0,len(pattern),k)]
	# print(seeds)
	seed_locations = set()

	shifted_matches = []
	for i,seed in enumerate(seeds):
		# print(i)
		result = BetterBWMatching(firstOccurrence,bwt,seed,Count)
		# print(result)
		if len(result) == 1:
			continue
		else:
			for j in range(result[0],result[1]+1):
				shifted_matches.append(suffixArray[j])
		# print(shifted_matches)
		shifted_matches = [shifted - k*i for shifted in shifted_matches]
		# print(shifted_matches)
		shifted_matches = [shifted for shifted in shifted_matches if shifted >= 0 and shifted + len(pattern) <= len(bwt)-1]
		# print(shifted_matches)

		seed_locations |= set(shifted_matches)
	return seed_locations




def seed_extension(text, pattern, seed_index, d):
	'''Determines if a seed location can be extended to the approximate pattern, returning the corresponding Boolean.'''
	count = 0
	for i in range(len(pattern)):
		if pattern[i] != text[seed_index+i]:
			count += 1
			if count > d:  # Can't extend if we have more than d mismatches.
				return False
	return True


if __name__ == '__main__':
	# with open('./data/BetterBWMatching_test.txt') as f:
	# 	text = f.readline().strip()
	# 	patterns = f.readline().strip().split()
	# text = 'AATCGGGTTCAATCGGGGT'
	# text = 'smnpbnnaaaaa$a'
	# patterns = ['ATCG', 'GGGT']
	# with open('./data/MultipleMatching_test.txt') as f:
	# 	text = f.readline().strip()
	# 	patterns = f.readlines()
	# patterns = [pattern.strip() for pattern in patterns]
	# s = GetPatternCount(text,patterns)
	# s = MultipleMatching(text,patterns)
	# print(' '.join(map(str,s)))
	# print(' '.join(map(str,sorted(s))))

	# text = 'ACATGCTACTTT'
	# patterns = ['ATT', 'GCC', 'GCTA', 'TATT']
	# d = 1
	# with open('./data/MultipleApproximatePatternMatching_test.txt') as f:
	# 	text = f.readline().strip()
	# 	patterns = f.readline().strip().split()
	# 	d = int(f.readline().strip())
	# print(patterns)
	# print(patterns[0])
	# s = MultipleApproximatePatternMatching(text,patterns,d)
	# for ss in s:
	# 	print(ss)
	# print(' '.join(map(str,sorted(s))))

	# with open('result1.txt') as f:
	# 	line = f.readline().strip().split()
	# for s in line:
	# 	print(s)
	# text = 'banana$'
	# print(SuffixArray(text))
	# print(SuffixArray(text).values())

	text = 'CGTTTGCTAT$'
	print(BurrowsWheelerTransformation(text))