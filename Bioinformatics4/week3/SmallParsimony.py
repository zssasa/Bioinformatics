# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

from pprint import pprint
import numpy as np
import copy

def hamming(s1,s2):
	assert len(s1) == len(s2)
	d = 0
	for i in range(len(s1)):
		if s1[i]!=s2[i]:
			d+=1
	return d


def parsing_large_parsimony_problem_input(lines):
	n = int(lines[0])
	labels = []
	edges = []
	for l in lines[1:]:
		a = l.split('->')[0]
		b = l.split('->')[1]
		if a.isdigit() == True:
			a = int(a)
		else:
			if a not in labels:
				labels.append(a)
			a = labels.index(a)
		if b.isdigit() == True:
			b = int(b)
		else:
			if b not in labels:
				labels.append(b)
			b = labels.index(b)
		edges.append((a,b))
	return n,edges,labels



def small_parsimony_problem(n, edges, labels):
	m = 2*n - 1

	tree = {}
	parent = {}
	for edge in edges:
		node = edge[0]
		child =  edge[1]
		tree.setdefault(node,[]).append(child)
		parent[child] = node

	# pprint(tree)
	# pprint(parent)

	root = parent[list(parent.keys())[0]]
	# print(root)
	while root in parent:
		root = parent[root]

	l = len(labels[0])
	alphabet = sorted(list(set(''.join(labels))))
	# print(alphabet)
	k = len(alphabet)
	d = dict(zip(alphabet,range(k)))
	# print(d)

	s = [[' ']*l for _ in range(m)]
	sk = np.ndarray(shape=(m,k,l), dtype=int)
	sk.fill((m-1)*l)

	for i,label in enumerate(labels):
		s[i] = list(label)
		for j,c in enumerate(label):
			sk[i,d[c],j] = 0
	# print(sk)

	for i in range(l):
		def dfs_sk(node):
			if node<n:
				return
			lnode = tree[node][0]
			rnode = tree[node][1]
			dfs_sk(lnode)
			dfs_sk(rnode)
			for j in range(k):
				mask = np.ones(k)
				mask[j] = 0
				sk[node,j,i] = min(sk[lnode,:,i]+mask) + min(sk[rnode,:,i]+mask)
			return
		dfs_sk(root)

	parsimony = sum(sk[root].min(axis=0))


	for i in range(l):
		def dfs_s(node):
			if node <n:
				return
			c = sk[node,:,i]
			if node == root:
				s[node][i]=alphabet[c.argmin()]
			else:
				pnode = parent[node]
				j = d[s[pnode][i]]
				mask = np.ones(k,dtype=int)
				mask[j] = 0
				# mask = np.int(mask)
				# print(type(c))
				# print(type(mask))
				c+=mask
				s[node][i] = alphabet[c.argmin()]
			lnode = tree[node][0]
			rnode = tree[node][1]
			dfs_s(lnode)
			dfs_s(rnode)
		dfs_s(root)
	ret = []
	for node,(lnode,rnode) in tree.items():
		ps = ''.join(s[node])
		ls = ''.join(s[lnode])
		rs = ''.join(s[rnode])
		ret.append((ps,ls))
		ret.append((ps,rs))
	lbranch = (''.join(s[root]), ''.join(s[tree[node][0]]))
	rbranch = (''.join(s[root]), ''.join(s[tree[node][1]]))
	return (parsimony,ret[:],rbranch,lbranch)

def small_parsimony_unrooted_problem(n,uedges,labels):
	'''
	CODE CHALLENGE: Solve the Small Parsimony in an Unrooted Tree Problem.
	Input: An integer n followed by an adjacency list for an unrooted binary tree with n leaves
	labeled by DNA strings.
	Output: The minimum parsimony score of this tree, followed by the adjacency list of the
	tree corresponding to labeling internal nodes by DNA strings in order to minimize the
	parsimony score of the tree.
	'''
	# compute unrooted tree from edges
	utree = {}
	m = n+1
	for uedge in uedges:
		node = uedge[0]
		child = uedge[1]
		m = max(node+1,child+1,m)
		utree.setdefault(node,[]).append(child)

	# m, total node count

	 # given edge create a rooted tree from unrooted tree
	def get_rooted_tree(uedge):
		(lnode,rnode) = uedge
		root = m
		visited = [False]*(m+1)
		edges = []
		rooted_tree = copy.deepcopy(utree)
		rooted_tree[rnode].remove(lnode)
		rooted_tree[lnode].remove(rnode)
		rooted_tree[root] = [lnode,rnode]
		def dfs_rooted_tree(node):
			if (node < n) or (visited[node] == True):
				# tree bottom or already visited, simply return
				return
			visited[node] = True
			for child in rooted_tree[node]:
				if (visited[child] == False ):
					edges.append((node,child))
					dfs_rooted_tree(child)
			return
		dfs_rooted_tree(root)
		return edges

	perls = []
	for uedge in set([(min(a,b),max(a,b)) for (a,b) in uedges]):
		edges = get_rooted_tree(uedge)
		perl = small_parsimony_problem(n,edges,labels)
		perls.append(perl)
	(p,e,r,l) = min(perls)
	# find root's children
	ret = [(edge[0],edge[1]) for edge in e if (edge != r and edge !=l)]
	ret.append((l[1],r[1]))
	return (p,ret)

def tree_nearest_neighbors(e,utree):
	'''
	CODE CHALLENGE: Solve the Nearest Neighbors of a Tree Problem.
	Input: Two internal nodes a and b specifying an edge e, followed by an adjacency
	list of an unrooted binary tree.
	Output: Two adjacency lists representing the nearest neighbors of the tree with
	respect to e. Separate the adjacency lists with a blank line.
	'''
	a = e[0]
	b = e[1]

	atree = utree[a][:]
	atree.remove(b)
	w = atree[0]
	x = atree[1]
	btree = utree[b][:]
	btree.remove(a)
	y = btree[0]
	z = btree[1]

	# print(w)
	# print(x)
	# print(z)
	# print(y)
	# neighbor utree1 is like wya <=>bxz :
	utree1 = copy.deepcopy(utree)
	utree1[a] = [b,y,w]
	utree1[y].remove(b)
	utree1[y].append(a)
	utree1[b] = [a,x,z]
	utree1[x].remove(a)
	utree1[x].append(b)

	# neighbor utree2 is like wza <=>bxy :
	utree2 = copy.deepcopy(utree)
	utree2[a] = [b,z,w]
	utree2[z].remove(b)
	utree2[z].append(a)
	utree2[b] = [a,x,y]
	utree2[x].remove(a)
	utree2[x].append(b)
	return (utree1,utree2)



def edge2tree(edges):
	tree = {}
	for e in edges:
		node = e[0]
		child = e[1]
		tree.setdefault(node,[]).append(child)
	return tree

def tree2edge(tree):
	edges = []
	for node,children in tree.items():
		for child in children:
			edges.append((node,child))
	return edges


def large_parsimony_problem(n,edges,labels):
	'''
	CODE CHALLENGE: Implement the nearest neighbor interchange heuristic for the Large Parsimony Problem.
	Input: An integer n, followed by an adjacency list for an unrooted binary tree whose n leaves are
	labeled by DNA strings and whose internal nodes are labeled by integers.
	Output: The parsimony score and unrooted labeled tree obtained after every step of the nearest
	neighbor interchange heuristic. Each step should be separated by a blank line.
	'''
	# print '>>> go: !'
	(p,e) = small_parsimony_unrooted_problem(n,edges,labels)
	ret = [(p,e),]
	parsimony = p
	while True:
		minimum_achieved = True
		# print 'parsimony',parsimony
		candidate_edges = set([(a,b) for (a,b) in edges if a>=n and b>=n])
		# print(candidate_edges)
		for e in candidate_edges:
			# print e,len(candidate_edges)
			# if e[0] < n or e[1] < n:
				# simply skip leaves
				# continue
			edges1,edges2 = list(map(tree2edge, tree_nearest_neighbors(e, edge2tree(edges))))
			(p,e) = small_parsimony_unrooted_problem(n,edges1,labels)
			if p < parsimony:
				parsimony = p
				nedges = edges1
				# nedges = e
				minimum_achieved = False
			(p,e) = small_parsimony_unrooted_problem(n,edges2,labels)
			if p < parsimony:
				parsimony = p
				# nedges = e
				nedges = edges2
				minimum_achieved = False
		if minimum_achieved == True:
			break
		else:
			edges = nedges
			(p,e) = small_parsimony_unrooted_problem(n,edges,labels)
			ret.append((p,e))

	return ret

if __name__ == '__main__':
	# with open('./data/SmallParsimony_test.txt') as f:
	# with open('./data/Small_Parsimony_Unrooted_Tree_test.txt') as f:
	with open('./data/Large_Parsimony_Heuristic_with_NNI_test.txt') as f:
		lines = f.readlines()
	lines = [line.strip() for line in lines]
	n,edges,labels = parsing_large_parsimony_problem_input(lines)
	# print(edges)
	# print(labels)
	# (p,e,r,l) = SmallParismony(n,edges,labels)
	# print(p)
	# for ee in e:
	# 	print('%s->%s:%d'%(ee[0],ee[1],hamming(ee[0],ee[1])))
	# 	print('%s->%s:%d'%(ee[1],ee[0],hamming(ee[0],ee[1])))
	# print(e)
	# print(r)
	# print(l)
	# lines = [line.strip() for line in lines]
	# graph = adjToGraph(lines)
	# pprint(graph)
	# p,ret = small_parsimony_unrooted_problem(n,edges,labels)
	# print(p)
	# print(ret)
	# for ee in ret:
	# 	print('%s->%s:%d'%(ee[0],ee[1],hamming(ee[0],ee[1])))
	# 	print('%s->%s:%d'%(ee[1],ee[0],hamming(ee[0],ee[1])))
	#
	ret = large_parsimony_problem(n,edges,labels)
	# print(ret)
	for result in ret[1:]:
		print(result[0])
		for edge in result[1]:
			print('%s->%s:%d' %(edge[0],edge[1],hamming(edge[0],edge[1])))
			print('%s->%s:%d' %(edge[1],edge[0],hamming(edge[0],edge[1])))
		print()


	# utree = {}
	# with open('./data/Nearest_Neighbors_test.txt') as f:
	# 	e = list(map(int,f.readline().strip().split()))
	# 	lines = f.readlines()
	#
	# for line in lines:
	# 	line = line.strip()
	# 	node1, node2 = list(map(int,line.split('->')))
	# 	utree.setdefault(node1,[]).append(node2)
	# utree1, utree2 = tree_nearest_neighbors(e,utree)
	# # print(utree1)
	# for key in utree1:
	# 	for value in utree1[key]:
	# 		print('%d->%d' %(key,value))
	# print()
	# for key in utree2:
	# 	for value in utree2[key]:
	# 		print('%d->%d' %(key,value))

