'''You are given an integer array arr[], the task is to find the maximum of minimum values for every window size k where 1≤ k ≤ arr.size(). For each window size k, consider all contiguous subarrays of length k, determine the minimum element in each subarray, and then take the maximum among all these minimums.
Return the results as an array, where the element at index i represents the answer for window size i+1.

Input: arr[] = [10, 20, 30, 50, 10, 70, 30]
Output: [70, 30, 20, 10, 10, 10, 10] 
Explanation: 
Window size 1: minimums are [10, 20, 30, 50, 10, 70, 30], maximum of minimums is 70.
Window size 2: minimums are [10, 20, 30, 10, 10, 30], maximum of minimums is 30.
Window size 3: minimums are [10, 20, 10, 10, 10], maximum of minimums is 20.
Window size 4–7: minimums are [10, 10, 10, 10], maximum of minimums is 10.

Input: arr[] = [10, 20, 30]
Output: [30, 20, 10]

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106'''

class Solution:
    def maxOfMins(self, arr):
        left=[-1]*len(arr)
        right=[len(arr)]*len(arr)
        
        stack=[]
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                left[i]=stack[-1]
            stack.append(i)
                
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1]
            stack.append(i)       
            
        ans=[0]*(len(arr))
        
        for i in range(len(arr)):
            size=right[i]-left[i]-2
            ans[size]=max(ans[size],arr[i])

        for i in range(len(arr)-2,-1,-1):
            ans[i]=max(ans[i+1],ans[i])
            
        return ans
