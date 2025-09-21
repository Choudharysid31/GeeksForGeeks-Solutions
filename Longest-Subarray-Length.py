'''You are given an array of integers arr[]. Your task is to find the length of the longest subarray such that all the elements of the subarray are smaller than or equal to the length of the subarray.

Input: arr[] = [1, 2, 3]
Output: 3
Explanation: The longest subarray is the entire array itself, which has a length of 3. All elements in the subarray are less than or equal to 3.

Input: arr[] = [6, 4, 2, 5]
Output: 0
Explanation: There is no subarray where all elements are less than or equal to the length of the subarray. The longest subarray is empty, which has a length of 0.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 109'''

class Solution:
    def longestSubarray(self, arr):
       
        left=[-1]*len(arr)
        right=[len(arr)]*len(arr)
        
        lstack=[]
        for i in range(len(arr)):
            
            while lstack and arr[lstack[-1]]<=arr[i]:
                lstack.pop()
            if lstack:
                left[i]=lstack[-1]
            lstack.append(i)
            
        rstack=[]
        for i in range(len(arr)-1,-1,-1):
            
            while rstack and arr[rstack[-1]]<arr[i]:
                rstack.pop()
            if rstack:
                right[i]=rstack[-1]
            rstack.append(i)
            
        ans=0
        check=0
        
        for i in range(len(arr)):
            check=right[i]-left[i]-1
            if check>=arr[i]:
                ans=max(ans,check)

        return ans
