'''You are given an array coins[], where each element represents a coin of a different denomination, and a target value sum. You have an unlimited supply of each coin type {coins1, coins2, ..., coinsm}.
Your task is to determine the minimum number of coins needed to obtain the target sum. If it is not possible to form the sum using the given coins, return -1.

Input: coins[] = [25, 10, 5], sum = 30
Output: 2
Explanation: Minimum 2 coins needed, 25 and 5  

Input: coins[] = [5, 1], sum = 0
Output: 0
Explanation: For 0 sum, we do not need a coin

Input: coins[] = [4, 6, 2], sum = 5
Output: -1
Explanation: Not possible to make the given sum.'''


class Solution:
	def minCoins(self, coins, sum):
		dp=[float("inf")]*(sum+1)
		dp[0]=0
		for coin in coins:
		    for j in range(coin,sum+1):
		        dp[j]=min(dp[j],1+dp[j-coin])
	    return dp[-1] if dp[-1]!=float("inf") else -1
