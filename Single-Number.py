'''Given an array arr[] of positive integers where every element appears even times except for one. Find that number occurring an odd number of times.

Input: arr[] = [1, 1, 2, 2, 2]
Output: 2
Explanation: In the given array all element appear two times except 2 which appears thrice.

Input: arr[] = [8, 8, 7, 7, 6, 6, 1]
Output: 1
Explanation: In the given array all element appear two times except 1 which appears once.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''

class Solution:   
    def getSingle(self,arr):
        res=0
        for i in arr:
            res^=i
        return res
