'''Given an array arr of size n and an integer x. Find if there's a triplet in the array which sums up to the given integer x.

Examples
Input:n = 6, x = 13, arr[] = [1,4,45,6,10,8]
Output: 1
Explanation: The triplet {1, 4, 8} in the array sums up to 13.

Input: n = 6, x = 10, arr[] = [1,2,4,3,6,7]
Output: 1
Explanation: Triplets {1,3,6} & {1,2,7} in the array sum to 10. 

Input: n = 6, x = 24, arr[] = [40,20,10,3,6,7]
Output: 0
Explanation: There is no triplet with sum 24.

Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)'''

class Solution:
    def find3Numbers(self, arr, n, x):
        arr.sort()
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                if arr[i]+arr[j]+arr[k]==x:
                    return 1
                elif arr[i]+arr[j]+arr[k]>x:
                    k-=1
                else:
                    j+=1
        return 0
