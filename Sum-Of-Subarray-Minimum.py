'''Given an array arr[] of positive integers, find the total sum of the minimum elements of every possible subarrays.

Input: arr[] = [3, 1, 2, 4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3, 1], [1, 2], [2, 4], [3, 1, 2], [1, 2, 4], [3, 1, 2, 4]. Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1. Sum of all these is 17.

Input: arr[] = [71, 55, 82, 55]
Output: 593

1 ≤ arr.size() ≤ 3*104
1 ≤ arr[i] ≤ 103'''

class Solution:
    def sumSubMins(self, arr):
        left=[-1]*len(arr)
        right=[len(arr)]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                left[i]=stack[-1]
            stack.append(i)

        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1]
            stack.append(i)

        ans=0
        for i in range(len(arr)):
            ans+=arr[i]*(i-left[i])*(right[i]-i)
        
        return ans
