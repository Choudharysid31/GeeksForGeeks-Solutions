'''Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Input: arr[] = {15,-2,2,-8,1,7,10,23}, n = 8
Output: 5
Explanation: The largest subarray with sum 0 is -2 2 -8 1 7.

Input: arr[] = {2,10,4}, n = 3
Output: 0
Explanation: There is no subarray with 0 sum.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).'''

class Solution:
    def maxLen(self, n, arr):
        out={}
        longest=0
        sume=0
        k=0
        for end in range(n):
            sume+=arr[end]
            if sume==k:
                longest=end+1
            if sume-k in out:
                longest=max(longest,end-out[sume-k])
            if sume not in out:
                out[sume]=end
        return longest
