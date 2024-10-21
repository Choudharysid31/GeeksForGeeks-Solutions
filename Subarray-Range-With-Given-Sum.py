'''Given an unsorted array of integers arr[], and a target tar, determine the number of subarrays whose elements sum up to the target value.

Input: arr[] = [10, 2, -2, -20, 10] , tar = -10
Output: 3
Explanation: Subarrays with sum -10 are: [10, 2, -2, -20], [2, -2, -20, 10] and [-20, 10].

Input: arr[] = [1, 4, 20, 3, 10, 5] , tar = 33
Output: 1
Explanation: Subarray with sum 33 is: [20,3,10].

Expected Time Complexity: O(n)
Expected Auxilary Space: O(n)'''

class Solution:
    def subArraySum(self,arr, tar):
        out={}
        count=0
        sume=0
        for end in arr:
            sume+=end
            if sume==tar:
                count+=1
            if sume-tar in out:
                count+=out[sume-tar]
            if sume not in out:
                out[sume]=1
            else:
                out[sume]+=1
        return count
