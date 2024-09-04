'''Given a string str, find the longest palindromic substring in str. Substring of string str: str[ i . . . . j ] where 0 ≤ i ≤ j < len(str). Return the longest palindromic substring of str.
Palindrome string: A string that reads the same backward. More formally, str is a palindrome if reverse(str) = str. In case of conflict, return the substring which occurs first ( with the least starting index).

Examples :
Input: str = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic substring is "aabbaa".
Input: str = "abc"
Output: a
Explanation: "a", "b" and "c" are the longest palindromes with same length. The result is the one with the least starting index.

Expected Time Complexity: O(|str|2).
Expected Auxiliary Space: O(1).'''

class Solution:
    def longestPalin(self, S):
        if len(S)<2:
            return S
        large=S[0]
        maxi=0
        for i in range(len(S)):
            start=i
            end=i+1
            while start>=0 and end<len(S) and S[start]==S[end]:
                if maxi<(end-start+1):
                    large=S[start:end+1]
                    maxi=end-start+1
                start-=1
                end+=1
            
        for i in range(len(S)):
            start=i-1
            end=i+1
            while start>=0 and end<len(S) and S[start]==S[end]:
                if maxi<(end-start+1):
                    large=S[start:end+1]
                    maxi=end-start+1
                start-=1
                end+=1
        return large
