'''Given two sorted arrays of distinct integers arr1 and arr2. Each array may have some elements in common with the other array. Find the maximum sum of a path from the beginning of any array to the end of any array. You can switch from one array to another array only at the common elements.
Note:  When we switch from one array to other,  we need to consider the common element only once in the result.

Input: arr1 = [2, 3, 7, 10, 12] , arr2 = [1, 5, 7, 8]
Output: 35
Explanation: The path will be 1+5+7+10+12 = 35, where 1 and 5 come from arr2 and then 7 is common so we switch to arr1 and add 10 and 12.
Input: arr1 = [1, 2, 3] , arr2[] = [3, 4, 5]
Output: 15
Explanation: The path will be 1+2+3+4+5=15.
Expected Time Complexity: O(m + n)
Expected Auxiliary Space: O(1)'''

class Solution:
    def maxPathSum(self, arr1, arr2):
        n=len(arr1)
        m=len(arr2)
        i=0
        j=0
        sum1=0
        sum2=0
        final=0
        while (i<n and j<m):
            if arr1[i]<arr2[j]:
                sum1+=arr1[i]
                i+=1
            elif arr1[i]>arr2[j]:
                sum2+=arr2[j]
                j+=1
            else:
                final+=max(sum1,sum2)+arr1[i]
                sum1=0
                i+=1
                sum2=0
                j+=1
        while (i<n):
            sum1+=arr1[i]
            i+=1
        while (j<m):
            sum2+=arr2[j]
            j+=1
        final+=max(sum1,sum2)
        return final
