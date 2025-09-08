'''Given an array arr[] of positive integers, your task is to find the maximum possible sum of all elements that are not part of the Longest Increasing Subsequence (LIS).

Input: arr[] = [4, 6, 1, 2, 3, 8]
Output: 10
Explanation: The elements which are not in LIS is 4 and 6.

Input: arr[] = [5, 4, 3, 2, 1]
Output: 14
Explanation: The elements which are not in LIS is 5, 4, 3 and 2.

Constraints:
1 ≤ arr.size() ≤ 103
1 ≤ arr[i] ≤ 105'''

class Solution:
    def nonLisMaxSum(self, arr):
        dp=[1]*len(arr)
        dpsum=arr[:]
        sume=0
        for i in range(1,len(arr)):
            for j in range(i):
                if (arr[i]>arr[j] and dp[i]<dp[j]+1):
                    dp[i]=dp[j]+1
                    dpsum[i]=dpsum[j]+arr[i]
                elif(dp[i]==dp[j]+1):
                    dpsum[i]=min(dpsum[i],dpsum[j]+arr[i])
                    
        total=sum(arr)
        maxi=-float("inf")
        sumi=0
        
        for i in range(len(arr)):
            if dp[i]>maxi:
                maxi=dp[i]
                sumi=dpsum[i]
            elif dp[i]==maxi:
                sumi=min(sumi,dpsum[i])
                
        return total-sumi
