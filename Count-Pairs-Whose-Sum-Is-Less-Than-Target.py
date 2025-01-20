'''Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly less than the target.

Input: arr[] = [7, 2, 5, 3], target = 8
Output: 2
Explanation: There are 2 pairs with sum less than 8: (2, 5) and (2, 3). 

Input: arr[] = [5, 2, 3, 2, 4, 1], target = 5
Output: 4
Explanation: There are 4 pairs whose sum is less than 5: (2, 2), (2, 1), (3, 1) and (2, 1).

Input: arr[] = [2, 1, 8, 3, 4, 7, 6, 5], target = 7
Output: 6
Explanation: There are 6 pairs whose sum is less than 7: (2, 1), (2, 3), (2, 4), (1, 3), (1, 4) and (1, 5).'''

class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        ans=0
        left=0
        right=len(arr)-1
        while left<right:
            if arr[left]+arr[right]<target:
                ans+=(right-left)
                left+=1
            else:
                right-=1
        return ans
