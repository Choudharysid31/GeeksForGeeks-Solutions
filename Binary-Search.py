'''Given a sorted array arr and an integer k, find the position(0-based indexing) at which k is present in the array using binary search.
Examples:

Input: k = 4, arr= [1, 2, 3, 4, 5]  
Output: 3
Explanation: 4 appears at index 3.

Input: k = 445, arr= [11, 22, 33, 44, 55] 
Output: -1
Explanation: 445 is not present.'''

class Solution:
    def binarysearch(self, arr, k):
        left=0
        right=len(arr)-1
        while left<=right:
            mid= left+ (right-left)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]<k:
                left=mid+1
            else:
                right=mid-1
        return -1
