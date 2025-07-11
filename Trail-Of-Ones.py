'''Given an integer n, the task is to count the number of binary strings of length n that contains at least one pair of consecutive 1's.
Note: A binary string is a sequence made up of only 0's and 1's.

Input: n = 2
Output: 1
Explanation: There are 4 strings of length 2, the strings are 00, 01, 10, and 11. Only the string 11 has consecutive 1's.

Input: n = 3
Output: 3
Explanation: There are 8 strings of length 3, the strings are 000, 001, 010, 011, 100, 101, 110 and 111. The strings with consecutive 1's are 011, 110 and 111.

Input: n = 5
Output: 19
Explanation: There are 19 strings having at least one pair of consecutive 1's.

2 ≤ n ≤ 30'''

class Solution:
    def countConsec(self, n: int) -> int:
        first,second=1,1
        for i in range(2,n+1):
            #modified fibbonacci
            first,second=second,first+second
            
        return 2**n -(second+first)
