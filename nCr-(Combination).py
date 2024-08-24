'''Given two integers n and r, find nCr. Since the answer may be very large, calculate the answer modulo 109+7.

Input: n = 3, r = 2
Output: 3
Explaination: 3C2 = 3. 

Input: n = 2, r = 4
Output: 0
Explaination: r is greater than n.

Expected Time Complexity: O(n*r)
Expected Auxiliary Space: O(r)'''

class Solution:
    def nCr(self, n, r):
        if n<r:
            return 0
        if r==0:
            return 1
        if n==r:
            return 1
        num=1
        denom=1
        for i in range(1,r+1):
            denom*=i
        for j in range(1,r+1):
            num=num*((j+(n-r)))
        return (num//denom)%1000000007
