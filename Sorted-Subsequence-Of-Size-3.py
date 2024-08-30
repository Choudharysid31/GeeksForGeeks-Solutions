'''You are given an array arr, you need to find any three elements in it such that arr[i] < arr[j] < arr[k] and i < j < k.

Note: The output will be 1 if the subsequence returned by the function is present in the array arr
If the subsequence is not present in the array then return an empty array, the driver code will print 0.
If the subsequence returned by the function is not in the format as mentioned then the output will be -1.

Input: arr = [1, 2, 1, 1, 3]
Output: 1
Explanation: A subsequence 1 2 3 exist.

Input: arr = [1, 1, 3]
Output: 0
Explanation: No such Subsequence exist, so empty array is returned (the driver code automatically prints 0 in this case).

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)'''

class Solution:
    def find3Numbers(self, arr):
        if len(arr)<3:
            return []
        left=[arr[0]]
        right=[0]*len(arr)
        right[n-1]=arr[n-1]
        for i in range(1,n):
            left.append(min(left[i-1],arr[i]))
        for j in range(n-2,-1,-1):
            right[j]=max(right[j+1],arr[j])
        for i in range(1,n-1):
            if left[i-1]<arr[i]<right[i+1]:
                return ([left[i-1],arr[i],right[i+1]])
        return []
