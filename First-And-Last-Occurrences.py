'''Given a sorted array arr containing n elements with possibly some duplicate, the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.

Input: n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  2 5
Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5. 

Input:n=9, x=7
arr[] = { 1, 3, 5, 5, 5, 5, 7, 123, 125 }
Output:  6 6
Explanation: First and last occurrence of 7 is at index 6.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1).'''

class Solution:
    def find(self, arr, n, x):
        left=0
        right=n
        while left<=right:
            mid=left+(right-left)//2
            if arr[mid]==x:
                start=mid-1
                end=mid+1
                while start>-1 and arr[mid]==arr[start]:
                    start-=1
                while end<n and arr[mid]==arr[end]:
                    end+=1
                return(start+1,end-1)
            elif arr[mid]>x:
                right=mid-1
            else:
                left=mid+1
        return (-1,-1)
        
