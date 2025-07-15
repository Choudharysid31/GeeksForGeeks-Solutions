'''Given an array arr[], return true if there is a triplet (a, b, c) from the array (where a, b, and c are on different indexes) that satisfies a2 + b2 = c2, otherwise return false.

Input: arr[] = [3, 2, 4, 6, 5]
Output: true
Explanation: a=3, b=4, and c=5 forms a pythagorean triplet.

Input: arr[] = [3, 8, 5]
Output: false
Explanation: No such triplet possible.

Input: arr[] = [1, 1, 1]
Output: false

1 <= arr.size() <= 105
1 <= arr[i] <= 103'''

class Solution:
	def pythagoreanTriplet(self, arr):
	    arr=sorted(list(set(arr)),reverse=True)
	    
	    for i in range(len(arr)):
	        x=arr[i]**2
	        y=i+1
	        z=len(arr)-1
	        while y<z:
	            if arr[z]**2+arr[y]**2>x:
	                y+=1
	            elif arr[z]**2+arr[y]**2<x:
	                z-=1
	            else:
	                return True
	                
	    return False
