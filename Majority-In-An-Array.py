'''Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears strictly more than N/2 times in the array.

Input: N = 3 
A[] = {1,2,3} 
Output:-1
Explanation: Since, each element in {1,2,3} appears only once so there is no majority element.

Input: N = 5 
A[] = {3,1,3,3,2} 
Output: 3
Explanation: Since, 3 is present more than N/2 times, so it is the majority element.'''


class Solution:
    def majorityElement(self, arr):
        major=arr[0]
        count=1
        for i in range(1,len(arr)):
            if (major==arr[i]):
                count+=1
            else:
                count-=1
            if count==0:
                major=arr[i]
                count=1
        if arr.count(major)>len(arr)//2:
            return major
        return -1
