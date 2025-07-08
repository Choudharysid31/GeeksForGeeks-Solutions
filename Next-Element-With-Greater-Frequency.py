'''Given an array arr[] of integers, for each element, find the closest (distance wise) to its right that has a higher frequency than the current element. If no such element exists, return -1 for that position.

Input: arr[] = [2, 1, 1, 3, 2, 1]
Output: [1, -1, -1, 2, 1, -1]
Explanation: Frequencies: 1 → 3 times, 2 → 2 times, 3 → 1 time.
For arr[0] = 2, the next element 1 has a higher frequency → 1.
For arr[1] and arr[2], no element to the right has a higher frequency → -1.
For arr[3] = 3, the next element 2 has a higher frequency → 2.
For arr[4] = 2, the next element 1 has a higher frequency → 1.
For arr[5] = 1, no elements to the right → -1.

Input: arr[] = [5, 1, 5, 6, 6]
Output: [-1, 5, -1, -1, -1]

1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105'''

class Solution:
    def findGreater(self, arr):
        dicti={}
        for i in arr:
            dicti[i]=dicti.get(i,0)+1
        stack=[]
        ans=[-1]*len(arr)

        for i in range(len(arr)-1,-1,-1):
            
            while stack and dicti[stack[-1]]<=dicti[arr[i]]:
                stack.pop()
              
            if stack:
                ans[i]=stack[-1]
                
            stack.append(arr[i])
        
        return ans
