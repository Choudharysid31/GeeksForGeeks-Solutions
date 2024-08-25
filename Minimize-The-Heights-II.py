'''Given an array arr[] denoting heights of N towers and a positive integer K. For each tower, you must perform exactly one of the following operations exactly once.
Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

Example 1:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output: 5
Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}. The difference between the largest and the smallest is 8-3 = 5.

Example 2:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output:11
Explanation: The array can be modified as {3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}. The difference between the largest and the smallest is 17-6 = 11. 

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)'''
class Solution:
    def getMinDiff(self, arr, n, k):
        if n==1:
            return 0
        arr.sort()
        mini=arr[-1]-arr[0]
        for i in range(1,n):
            if arr[i]<k:
                continue
            curr_min=min(arr[0]+k,arr[i]-k)
            curr_max=max(arr[n-1]-k,arr[i-1]+k)
            mini=min(mini,curr_max-curr_min)
        return mini
