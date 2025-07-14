'''Given an increasing sorted rotated array arr of distinct integers. The array is right-rotated k times. Find the value of k.
Let's suppose we have an array arr = [2, 4, 6, 9], so if we rotate it by 2 times so that it will look like this:
After 1st Rotation : [9, 2, 4, 6]
After 2nd Rotation : [6, 9, 2, 4]

Input: arr = [5, 1, 2, 3, 4]
Output: 1
Explanation: The given array is 5 1 2 3 4. The original sorted array is 1 2 3 4 5. We can see that the array was rotated 1 times to the right.

Input: arr = [1, 2, 3, 4, 5]
Output: 0
Explanation: The given array is not rotated.

1 ≤ arr.size() ≤105
1 ≤ arri ≤ 107'''

class Solution:
    def findKRotation(self, arr):
        count=0
        for i in range(len(arr)-1,0,-1):
            if (arr[i-1]<arr[i]):
                count+=1
            else:
                break
        return len(arr)-count-1
