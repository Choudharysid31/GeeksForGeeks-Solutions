'''Given an integer N, find its factorial. return a list of integers denoting the digits that make up the factorial of N.

Input: N = 5
Output: [1,2,0]
Explanation : 5! = 1*2*3*4*5 = 120

Input: N= 10
Output: [3,6,2,8,8,0,0]
Explanation : 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800

Expected Time Complexity : O(N2)
Expected Auxilliary Space : O(1)'''
class Solution:
    def factorial(self, N):
        fact=1
        for i in range(1,N+1):
            fact*=i
        return list(map(int, list(str(fact))))
