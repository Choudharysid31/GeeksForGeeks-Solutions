'''You are given two strings str1 and str2. Your task is to find the length of the longest common substring among the given strings.
Examples:
Input: str1 = "ABCDGH", str2 = "ACDGHR"
Output: 4
Explanation: The longest common substring is "CDGH" which has length 4.
Input: str1 = "ABC", str2 = "ACB"
Output: 1
Explanation: The longest common substrings are "A", "B", "C" all having length 1.

Expected Time Complexity: O(n*m).
Expected Auxiliary Space: O(n*m).'''

class Solution:
    def longestCommonSubstr(self, str1, str2):
        large=0
        for i in range(len(str1)-1):
            for j in range(i+1,len(str1)+1):
                if str1[i:j] in str2:
                    large=max(len(str1[i:j]),large)
        return large
