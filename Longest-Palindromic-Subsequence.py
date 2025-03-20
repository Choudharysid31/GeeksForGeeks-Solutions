'''Given a string s, return the length of the longest palindromic subsequence.A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.

Input: s = "bbabcbcab"
Output: 7
Explanation: Subsequence "babcbab" is the longest subsequence which is also a palindrome.

Input: s = "abcd"
Output: 1
Explanation: "a", "b", "c" and "d" are palindromic and all have a length 1.

Input: s = "agbdba"
Output: 5
Explanation: The longest palindromic subsequence is "abdba", which has a length of 5. The characters in this subsequence are taken from the original string "agbdba", and they maintain the order of the string while forming a palindrome.

Constraints:
1 ≤ s.size() ≤ 1000
The string contains only lowercase letters.'''

class Solution:

    def longestPalinSubseq(self, s):
        rev=s[::-1]
        dp=[[0]*(len(s)+1) for _ in range(len(s)+1)]
        
        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if (s[i-1]==rev[j-1]):
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return (dp[-1][-1])

