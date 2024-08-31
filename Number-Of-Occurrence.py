'''Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.If x is not present in the array (arr) then return 0.

Input: N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 4
Explanation: x = 2 occurs 4 times in the given array so the output is 4.

Input: N = 7, X = 4
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 0
Explanation: X = 4 is not present in the given array so the output is 0.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)'''

class Solution:
	def count(self,arr, n, x):
        left=0
        right=n-1
        while left<=right:
            mid=left+(right-left)//2
            if arr[mid]==x:
                start=mid-1
                end=mid+1
                while start>-1 and arr[mid]==arr[start]:
                    start-=1
                while end<n and arr[mid]==arr[end]:
                    end+=1
                end=end-1
                start+=1
                return(end-start+1)
            elif arr[mid]>x:
                right=mid-1
            else:
                left=mid+1
        return (0)
