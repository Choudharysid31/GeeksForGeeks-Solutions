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
