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
