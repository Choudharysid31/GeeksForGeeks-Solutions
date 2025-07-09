'''Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

Input: arr[] = [3, 0, 1, 0, 4, 0 2]
Output: 10
Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.

Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides.

1 < arr.size() < 105
0 < arr[i] < 103'''

class Solution:
    def maxWater(self, arr):
        left=1
        right=len(arr)-2
        lefty=arr[0]
        righty=arr[-1]
        res=0
        while left<=right:
            
            if (lefty<righty):
                
                lefty=max(lefty,arr[left])
                res+=lefty-arr[left]

                left+=1
            
            else:

                righty=max(righty,arr[right])
                res+=righty-arr[right]
                
                right-=1
        
        return res
