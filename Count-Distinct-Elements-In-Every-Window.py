'''Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output:  [3, 4, 4, 3]

Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]
Explanation: Window 1 of size k = 2 is 4 1. Number of distinct elements in this window are 2. 
Window 2 of size k = 2 is 1 1. Number of distinct elements in this window is 1. 

Input: arr[] = [1, 1, 1, 1, 1], k = 3
Output: [1, 1, 1]'''

class Solution:
    def countDistinct(self, arr, k):
        ans=[]
        for i in range(len(arr)-k+1):
            ans.append(len(set(arr[i:i+k])))
        return ans
