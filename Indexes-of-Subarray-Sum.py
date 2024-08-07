'''Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements) that has sum equal to s. 
You mainly need to return the left and right indexes(1-based indexing) of that subarray.
In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.
Examples:
Input: arr[] = [1,2,3,7,5], n = 5, s = 12
Output: 2 4
Explanation: The sum of elements from 2nd to 4th position is 12.
Input: arr[] = [7,2,1], n = 3, s = 2
Output: 2 2
Explanation: The sum of elements from 2nd to 2nd position is 2.
Input: arr[] = [5,3,4], n = 3, s = 2
Output: -1
Explanation: There is no subarray with sum 2'''

class Solution:
    def subArraySum(self,arr, n, s):
        start=0
        end=0
        sume=0
        for end in range(n):
            sume+=arr[end]
            while(sume>s and start<end):
                sume-=arr[start]
                start+=1
            if sume==s:
                return [start+1,end+1]
        return [-1]
