'''Given an integer n, return an array ans of size n + 1, where each element i (0 ≤ i ≤ n) represents the count of 1s in the binary form of i.

Input: n = 2
Output: [0, 1, 1]
Explanation: 0  --> 0, 1 --> 1, 2 --> 10

Input: n = 5
Output: [0, 1, 1, 2, 1, 2] 
Explanation: 0  --> 0, 1 --> 1, 2 --> 10, 3 --> 11, 4 --> 100, 5 --> 101'''

class Solution:
    def countBits(self, n : int) -> List[int]:
        ans=[0]*(n+1)
        for i in range(n+1):
            ans[i]=ans[i//2]+i%2
        return ans
        


