# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

def DPChange(money, Coins):
	MinNumCoins = [0] * (money+1)
	for i in range(1,money+1):
		MinNumCoins[i] = float("inf")
		for j in range(len(Coins)):
			if i>=Coins[j]:
				if MinNumCoins[i-Coins[j]]+1 <= MinNumCoins[i]:
					MinNumCoins[i] = MinNumCoins[i-Coins[j]]+1
	return MinNumCoins[money]

