'''You are given an array arr[] of integers. Your task is to find the maximum sum of the smallest and second smallest elements across all subarrays (of size >= 2) of the given array.

Input: arr[] = [4, 3, 5, 1]
Output: 8
Explanation: All subarrays with at least 2 elements and find the two smallest numbers in each:
[4, 3] → 3 + 4 = 7
[4, 3, 5] → 3 + 4 = 7
[4, 3, 5, 1] → 1 + 3 = 4
[3, 5] → 3 + 5 = 8
[3, 5, 1] → 1 + 3 = 4
[5, 1] → 1 + 5 = 6
Maximum Score is 8.
Input: arr[] = [1, 2, 3]
Output: 5

2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106'''

class Solution:
    def maxSum(self, arr):
        return max(arr[i]+arr[i+1] for i in range(len(arr)-1))
