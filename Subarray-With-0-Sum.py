'''Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum. You just need to return true/false depending upon whether there is a subarray present with 0-sum or not. Printing will be taken care by the driver code.

Input:
n = 5
arr = {4,2,-3,1,6}
Output: Yes
Explanation: 2, -3, 1 is the subarray with sum 0.

Input:
n = 5
arr = {4,2,0,1,6}
Output: Yes
Explanation: 0 is one of the element in the array so there exist a subarray with sum 0.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).'''

class Solution:
    def subArrayExists(self,arr,n):
        hash1={}
        curr=0
        for i in arr:
            curr+=i
            if curr==0:
                return True
            if curr-0 in hash1:
                return True
            hash1[curr]=i
        return False
