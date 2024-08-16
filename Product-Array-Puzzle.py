'''Given an array nums[], construct a Product Array nums[] such that nums[i] is equal to the product of all the elements of nums except nums[i].

Examples:

Input: nums[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: For i=0, P[i] = 3*5*6*2 = 180.
For i=1, P[i] = 10*5*6*2 = 600.
For i=2, P[i] = 10*3*6*2 = 360.
For i=3, P[i] = 10*3*5*2 = 300.
For i=4, P[i] = 10*3*5*6 = 900.

Input: nums[] = [12,0]
Output: [0, 12]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)'''

class Solution:
    def productExceptSelf(self, nums):
        #code here
        lprod=1
        rprod=1
        result=[]
        for i in range (len(nums)):
            result.append(lprod)
            lprod*=nums[i]
        for i in range (len(nums)-1,-1,-1):
            result[i]*=rprod
            rprod*=nums[i]
        return result
