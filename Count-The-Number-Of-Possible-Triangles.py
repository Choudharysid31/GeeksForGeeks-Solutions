'''Given an integer array arr[]. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle. 
A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.

Input: arr[] = [4, 6, 3, 7]
Output: 3
Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a possible triangle. 

Input: arr[] = [1, 2, 3]
Output: 0
Explanation: No triangles are possible.'''

class Solution:
    def countTriangles(self, arr):
        arr.sort()
        count=0
        for i in range(len(arr)-1,1,-1):
            left=0
            right=i-1
            while left<right:
                if arr[left]+arr[right]>arr[i]:
                    count+=right-left
                    right-=1
                else:
                    left+=1
        return count
                    
