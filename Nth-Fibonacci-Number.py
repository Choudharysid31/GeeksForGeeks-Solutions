'''Given a positive integer n, find the nth fibonacci number. Since the answer can be very large, return the answer modulo 1000000007.

Note: for the reference of this question take first fibonacci number to be 1.

Examples :

Input: n = 2
Output: 1 
Explanation: 1 is the 2nd number of fibonacci series.
Input: n = 5
Output: 5
Explanation: 5 is the 5th number of fibonacci series.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)'''

class Solution:
    def nthFibonacci(self, n : int) -> int:
        if n==1:
            return 0
        else:
            a=0
            b=1
            for i in range(1,n):
                fib=(a+b)%1000000007
                a=b
                b=fib
        return fib
