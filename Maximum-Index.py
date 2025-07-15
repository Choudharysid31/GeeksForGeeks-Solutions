'''Given an array arr of positive integers. You have to return the maximum of j - i such that arr[i] < arr[j] and i < j.

Input: arr[] = [1, 10]
Output: 1
Explanation: arr[0] < arr[1] so (j-i) is 1-0 = 1.

Input: arr[] = [5, 4, 3]
Output: 0

Input: arr[] = [34, 8, 10, 3, 2, 80, 30, 33, 1]
Output: 6
Explanation: In the given array arr[1] < arr[7] satisfying the required condition(arr[i] < arr[j]) thus giving the maximum difference of j - i which is 6(7-1).

1 ≤ arr.size ≤ 105
0 ≤ arr[i] ≤ 109'''

class Solution:
    def maxIndexDiff(self, arr):
        leftmin=arr[:]
        rightmax=arr[:]
        
        for i in range(1,len(arr)):
            leftmin[i]=min(leftmin[i-1],leftmin[i])
            
        for j in range(len(arr)-2,-1,-1):
            rightmax[j]=max(rightmax[j+1],rightmax[j])
            
        left=0
        right=0
        res=0
        while left<len(arr) and right<len(arr):
            if (leftmin[left]<=rightmax[right]):
                res=max(res,right-left)
                right+=1
            else:
                left+=1
                
        return res
