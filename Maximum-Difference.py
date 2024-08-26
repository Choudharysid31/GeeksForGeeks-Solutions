'''Given an integer array arr of integers, the task is to find the maximum absolute difference between the nearest left smaller element and the nearest right smaller element of every element in array arr. If for any component of the arr, the nearest smaller element doesn't exist then consider it as 0.

Input: arr = [2, 1, 8]
Output: 1
Explanation: left smaller array ls = [0, 0, 1], right smaller array rs = [1, 0, 0]. Maximum Diff of abs(ls[i] - rs[i]) = 1

Input: arr = [2, 4, 8, 7, 7, 9, 3]
Output: 4
Explanation: left smaller array ls = [0, 2, 4, 4, 4, 7, 2], right smaller rs = [0, 3, 7, 3, 3, 3, 0]. Maximum Diff of abs(ls[i] - rs[i]) = abs(7 - 3) = 4

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)'''

class Solution:
    def findMaxDiff(self, arr):
        # code here
        n=len(arr)
        lf=[]
        rf=[0]*n
        stack=[]
        for i in range(n):
            while stack and stack[-1]>=arr[i]:
                stack.pop()
            if stack:
                lf.append(stack[-1])
            else:
                lf.append(0)
            stack.append(arr[i])
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1]>=arr[i]:
                stack.pop()
            if stack:
                rf[i]=stack[-1]
            else:
                rf[i]=0
            stack.append(arr[i])
        diff=0
        for i in range(len(arr)):
            diff=max(diff,abs(lf[i]-rf[i]))
        return diff
