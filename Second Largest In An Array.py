class Solution:
	def print2largest(self,arr, n):
	    arr=sorted(set(arr))
	    if (len(arr))<2:
	        return -1
	    return arr[-2]
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1
