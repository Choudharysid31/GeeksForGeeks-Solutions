'''You are given a histogram represented by an array arr, where each element of the array denotes the height of the bars in the histogram. All bars have the same width of 1 unit.Your task is to find the largest rectangular area possible in the given histogram, where the rectangle can be formed using a number of contiguous bars.

Input: arr[] = [60, 20, 50, 40, 10, 50, 60]
Output: 100
Explanation: We get the maximum by picking bars highlighted above in green (50, and 60). The area is computed (smallest height) * (no. of the picked bars) = 50 * 2 = 100.

Input: arr[] = [3, 5, 1, 7, 5, 9]
Output: 15
Explanation:  We get the maximum by picking bars 7, 5 and 9. The area is computed (smallest height) * (no. of the picked bars) = 5 * 3 = 15.

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 104'''


class Solution:
    def getMaxArea(self,arr):
        
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
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            
            if stack:
                right[i]=stack[-1]
                
            stack.append(i)
            
        res=0
        maxi=0

        for i in range(len(arr)):
        
            res=arr[i]*(right[i]-left[i]-1)
            maxi=max(maxi,res)
            
        return maxi
