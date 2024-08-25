'''You are given two arrays arr1 and arr2. The task is to find the minimum value of arr1[0] * arr2[0] + arr1[1] * arr2[1] + .... + arr1[N-1] * arr2[N-1], where the shuffling of elements of arrays arr1 and arr2 is allowed.

Input: arr1 = [3, 1, 1] , arr2 = [6, 5, 4]
Output: 23 
Explanation: 1*6+1*5+3*4 = 6+5+12 = 23 is the minimum sum.

Input: arr1 = [6, 1, 9, 5, 4] , arr2 = [3, 4, 8, 2, 4]
Output: 80
Explanation: 2*9+3*6+4*5+4*4+8*1 = 18+18+20+16+8 = 80 is the minimum sum.

Expected Time Complexity: O(nlog(n))
Expected Auxiliary Space: O(1)'''
class Solution:
    def minValue(self, arr1, arr2):
        #code here
        arr1.sort()
        arr2.sort(reverse=True)
        res=0
        for i in range(len(arr1)):
            res+=arr1[i]*arr2[i]
        return res
