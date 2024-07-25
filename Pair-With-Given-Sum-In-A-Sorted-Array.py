'''You are given an integer k and an array arr[]. You have to find numbers of pairs in array arr[] which sums up to k. It is given that the elements of the array arr[] are
distinct and in sorted order.
Note: pair {a, b} and pair {b, a} are considered the same. Also, an element cannot pair with itself, i.e., pair {a, a} is invalid.
Example 1:
Input: k = 8, arr[] = [1, 2, 3, 4, 5, 6, 7]
Output: 3
Explanation: There are 3 pairs which sum up to 8 : {1, 7}, {2, 6}, {3, 5}'''

class Solution:
    def countPair (self, k, arr) : 
        i=0
        j=len(arr)-1
        count=0
        while i<j:
            if arr[i]+arr[j]==k:
                count+=1
                i+=1
                j-=1
            elif arr[i]+arr[j]>k:
                j-=1
            else:
                i+=1
        return count
