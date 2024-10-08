'''A number n can be broken into three parts n/2, n/3, and n/4 (consider only the integer part). Each number obtained in this process can be divided further recursively. Find the maximum sum that can be obtained by summing up the divided parts together.
Note: It is possible that we don't divide the number at all.

Input: n = 12
Output: 13
Explanation: Break n = 12 in three parts {12/2, 12/3, 12/4} = {6, 4, 3}, now current sum is = (6 + 4 + 3) = 13. Further breaking 6, 4 and 3 into parts will produce sum less than or equal to 6, 4 and 3 respectively.

Input: n = 24
Output: 27
Explanation: Break n = 24 in three parts {24/2, 24/3, 24/4} = {12, 8, 6}, now current sum is = (12 + 8 + 6) = 26 . But recursively breaking 12 would produce value 13. So our maximum sum is 13 + 8 + 6 = 27.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)'''

class Solution:
    def maxSum(self, n):
        dp=[0]*(n+1)
        for i in range(n+1):
            dp[i]=max(i,dp[i//2]+dp[i//3]+dp[i//4])
        return dp[-1]
        
