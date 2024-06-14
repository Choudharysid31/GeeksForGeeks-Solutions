'''Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.'''

class Solution:
    def sort012(self,arr,n):
        arr.sort()
        return arr
if __name__=="__main__":
  t=int(input())
  arr=[int(x) for x in input().strip().split()]
  ob=Solution()
  ob.sort12(arr,n)
  for i in arr:
    print(i, end='')
  print()
  
