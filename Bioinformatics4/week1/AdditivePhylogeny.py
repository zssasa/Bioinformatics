# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'


from LimbLength import LimbLength
from pprint import pprint


def find_path(adj,i,j):
	visited = [None] * (max(adj.keys())+1)
	def dfs(path):
		for (v,w) in adj[path[-1][0]]:
			if visited[v] == True:
				continue
			visited[v] = True
			pathlen = path[-1][1] + w
			npath = path[:]
			npath.append((v,pathlen))
			if (v == j):
				# found the node that ends path.
				return npath
			result = dfs(npath)
			if result is not None:
				return result
		return
	return dfs([(i,0)])

def find_condition(dist, l):
	for i in range(l):
		for j in range(i+1,l):
			if dist[i][j] == dist[i][l]+dist[j][l]:
				return (i,j)
	assert 0
	return



def add_leaf(adj,n,leaf,i,j,x,w):
	path = find_path(adj,i,j)
	parent = None
	for k in range(len(path)-1):
		if path[k][1] == x:
			parent = path[k][0]
			break
		if path[k][1] < x and x< path[k+1][1]:
			u = path[k][0]
			v = path[k+1][0]
			w0 = path[k+1][1] - path[k][1]
			w1 = x - path[k][1]
			w2 = path[k+1][1] - x
			parent = max(adj.keys()+[n-1]) + 1
			adj[u].remove((v,w0))
			adj[v].remove((u,w0))
			adj[parent] = []
			adj[u].append((parent,w1))
			adj[parent].append((u,w1))

			adj[v].append((parent,w2))
			adj[parent].append((v,w2))
			break
	adj.setdefault(leaf,[]).append((parent,w))
	adj[parent].append((leaf,w))

	return adj


def AdditivePhylogeny(dist,n):
	adj = {}
	if n == 2:
		adj[0] = [(1,dist[0][1])]
		adj[1] = [(0,dist[1][0])]
		return adj
	limb = LimbLength(dist,n-1)
	for i in range(n-1):
		dist[i][n-1] -= limb
		dist[n-1][i] -= limb
	(i,k) = find_condition(dist, n-1)
	x = dist[i][n-1]
	AdditivePhylogeny(dist,n-1)
	adj = add_leaf(adj,n,n-1,i,k,x,limb)
	return adj




if __name__ == '__main__':
	dist = []
	with open('./data/test.txt') as input:
		n = int(input.readline())
		for line in input.readlines():
			dist.append(list(map(int,line.split('\t'))))
	pprint(AdditivePhylogeny(dist,n))
