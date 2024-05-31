'''Given an array A of positive integers. Your task is to find the leaders in the array. An element of the array is a leader if it is greater than all the elements to 
its right side or if it is equal to the maximum element on its right side. The rightmost element is always a leader. 

Example 1:

Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.'''

class Solution:
    def leaders(self, A, N):
        #Code here
        leader=A[N-1]
        leaders=[leader]+[]
        for i in range(len(A)-1,0,-1):
            if A[i-1]>=leader:
                leader=A[i-1]
                leaders=[leader]+leaders
        return leaders

import math    
def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        A=obj.leaders(A,N)
        for i in A:
            print(i,end=" ")
        print()
        T-=1
if __name__=="__main__":
    main()
