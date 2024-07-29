'''Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array. 
It is given that all array elements are distinct.
Note:-  l and r denotes the starting and ending index of the array.

Example 1:
Input:
n = 6
arr[] = 7 10 4 3 20 15
k = 3
l=0 r=5
Output : 
7
Explanation :
3rd smallest element in the given 
array is 7.

Expected Time Complexity: O(n*log(n) )
Expected Auxiliary Space: O(log(n))
Constraints:
1 <= n <= 105
l = 0
r = N-1
1<= arr[i] <= 105
1 <= k <= n'''

class Solution:
    def kthSmallest(self,arr, l, r, k):
        arr.sort()
        return(arr[k-1])
