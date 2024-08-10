'''Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero. Return true, if there is at least one triplet following the condition else return false.
Examples:
Input: n = 5, arr[] = {0, -1, 2, -3, 1}
Output: 1
Explanation: 0, -1, and 1 form a triplet with a sum equal to 0.
Input: n = 3, arr[] = {1, 2, 3}
Output: 0
Explanation: No triplet with zero sum exists. 

Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)'''

class Solution:
    def findTriplets(self, arr, n):
        dict={}
        count=0
        for i in range(n-1):
            for j in range(i+1,n):
                if dict.get(-(arr[i]+arr[j])):
                    count+=1
                    break
            dict[arr[i]]=1
            if count:
                break
        return count
