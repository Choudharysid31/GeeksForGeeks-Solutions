'''Given an array arr[] consisting of positive integers, your task is to find the length of the longest subarray that contains at most two distinct integers.

Input: arr[] = [2, 1, 2]
Output: 3
Explanation: The entire array [2, 1, 2] contains at most two distinct integers (2 and 1). Hence, the length of the longest subarray is 3.

Input: arr[] = [3, 1, 2, 2, 2, 2]
Output: 5
Explanation: The longest subarray containing at most two distinct integers is [1, 2, 2, 2, 2], which has a length of 5.

1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105'''

class Solution:
    def totalElements(self, arr):
        left=0
        right=1
        checker={arr[0]:1}
        ans=1
        n=len(arr)
        while right<n:
            checker[arr[right]]=checker.get(arr[right],0)+1

            while len(checker)>2:
                checker[arr[left]]-=1
                if checker[arr[left]]==0:
                    del(checker[arr[left]])
                left+=1

            ans=max(ans,right-left+1)
            right+=1
        return ans
