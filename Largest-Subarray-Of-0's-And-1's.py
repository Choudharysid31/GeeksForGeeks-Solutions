'''Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.

Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.
Input: arr[] = [0, 0, 1, 1, 0]
Output: 4
Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.
Input: arr[] = [0]
Output: 0
Explnation: There is no subarray with an equal number of 0s and 1s.'''

class Solution:
    def maxLen(self, arr):
        sum1=0
        count=0
        dicti={}
        for i in range(0,len(arr)):
            if arr[i]==0:
                sum1-=1
            else:
                sum1+=1
            if sum1==0:
                count=i+1
            if sum1 in dicti:
                count=max(count,i-dicti[sum1])
            else:
                dicti[sum1]=i
        return count
