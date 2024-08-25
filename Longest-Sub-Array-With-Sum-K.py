'''Given an array arr containing n integers and an integer k. Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

Example 1:
arr[] = {10, 5, 2, 7, 1, 9}, k = 15
Output : 4
Explanation: The sub-array is {5, 2, 7, 1}.

Example 2:
arr[] = {-1, 2, 3}, k = 6
Output : 0
Explanation: There is no such sub-array with sum 6.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).'''
class Solution:
    def lenOfLongSubarr (self, arr, n, k) :
        out={}
        longest=0
        sume=0
        for end in range(n):
            sume+=arr[end]
            if sume==k:
                longest=end+1
            if sume-k in out:
                longest=max(longest,end-out[sume-k])
            if sume not in out:
                out[sume]=end
        return longest
