'''You are given an array arr[] of positive integers and an integer k, find the number of subarrays in arr[] where the count of distinct integers is at most k.

Input: arr[] = [1, 2, 2, 3], k = 2
Output: 9
Explanation: Subarrays with at most 2 distinct elements are: [1], [2], [2], [3], [1, 2], [2, 2], [2, 3], [1, 2, 2] and [2, 2, 3].

Input: arr[] = [1, 1, 1], k = 1
Output: 6
Explanation: Subarrays with at most 1 distinct element are: [1], [1], [1], [1, 1], [1, 1] and [1, 1, 1].

Input: arr[] = [1, 2, 1, 1, 3, 3, 4, 2, 1], k = 2
Output: 24
Explanation: There are 24 subarrays with at most 2 distinct elements.

1 ≤ arr.size() ≤ 2*104
1 ≤ k ≤ 2*104
1 ≤ arr[i] ≤ 109'''

class Solution:
    def countAtMostK(self, arr, k):
        left=0
        right=1
        checker={arr[0]:1}
        ans=1
        n=len(arr)
        while right<n:
            checker[arr[right]]=checker.get(arr[right],0)+1

            while len(checker)>k:
                checker[arr[left]]-=1
                if checker[arr[left]]==0:
                    del(checker[arr[left]])
                left+=1

            ans+=(right-left+1)
            right+=1
        return ans
