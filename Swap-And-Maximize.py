'''Given an array arr[ ] of positive elements. Consider the array as a circular array arr, meaning the element after the last element is the first element of the array. 
The task is to find the maximum sum of the absolute difference between consecutive elements with rearrangement of array elements allowed i.e. rearrangement of array elements 
in such order that  |a1 – a2| + |a2 – a3| + …… + |an-1 – an| + |an – a1| is maximized.
Examples:
Input: arr[] = [4, 2, 1, 8]
Output: 18
Explanation: Rearrangement done is [1, 8, 2, 4]. Sum of absolute difference between consecutive elements after 
rearrangement = |1 - 8| + |8 - 2| + |2 - 4| + |4 - 1| = 7 + 6 + 2 + 3 = 18.'''

class Solution:
    def maxSum(self,arr):
        arr.sort()
        arr1=[]
        i=0
        j=len(arr)-1
        while i<j:
            arr1.append(arr[i])
            arr1.append(arr[j])
            i+=1
            j-=1
        sume=0
        for i in range(len(arr1)):
            if i==len(arr1)-1:
                sume+=abs(arr1[i]-arr1[0])
            else:
                sume+=abs(arr1[i]-arr1[i+1])
        return sume
