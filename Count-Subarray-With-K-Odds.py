'''You are given an array arr[] of positive integers and an integer k. You have to count the number of subarrays that contain exactly k odd numbers.

Examples:

Input: arr[] = [2, 5, 6, 9], k = 2
Output: 2
Explanation: There are 2 subarrays with 2 odds: [2, 5, 6, 9] and [5, 6, 9].
Input: arr[] = [2, 2, 5, 6, 9, 2, 11], k = 2
Output: 8
Explanation: There are 8 subarrays with 2 odds: [2, 2, 5, 6, 9], [2, 5, 6, 9], [5, 6, 9], [2, 2, 5, 6, 9, 2], [2, 5, 6, 9, 2], [5, 6, 9, 2], [6, 9, 2, 11] and [9, 2, 11].
Constraint:
1 ≤ k ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 109'''

class Solution:
    def countSubarrays(self, arr, k):
        freq={0:1}
        count=0
        ans=0
        for ele in arr:
            if ele%2:
                count+=1
            if count-k in freq:
                ans+=freq[count-k]
                
            freq[count]=1+freq.get(count,0)
        
        return ans
