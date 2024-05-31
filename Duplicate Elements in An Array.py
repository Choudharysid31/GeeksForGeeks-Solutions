'''Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. 
Return the answer in ascending order. If no such element is found, return list containing [-1]. 

Note: The extra space is only for the array to be returned. Try and perform all operations within the provided array. 

Example 1:

Input:
N = 4
a[] = {0,3,1,2}
Output: 
-1
Explanation: 
There is no repeating element in the array. Therefore output is -1.'''


class Solution:
    def duplicates(self, arr, n):
        dups = []
        for i in arr :
            if abs(i)==2**30:
                i=0
            else:
                i=abs(i)
            if arr[i]>0:
                arr[i]=-arr[i]
            elif arr[i]==0:
                arr[i]=-2**30
            else:
                dups.append(i)
                
        return [-1] if not dups else sorted(list(set(dups)))
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()
