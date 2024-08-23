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
        zero=0
        two=n-1
        ptr=0
        while ptr<=two:
            if arr[ptr]==0:
                arr[zero],arr[ptr]=arr[ptr],arr[zero]
                zero+=1
                ptr+=1
            elif arr[ptr]==2:
                arr[two],arr[ptr]=arr[ptr],arr[two]
                two-=1
            else:
                ptr+=1
        return arr
        # code here


  
