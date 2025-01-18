'''Given a string s, find the length of the longest substring with all distinct characters. 

Input: s = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring with all distinct characters.

Input: s = "aaa"
Output: 1
Explanation: "a" is the longest substring with all distinct characters.

Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.'''

class Solution:
    def longestUniqueSubstr(self, s):
        new={s[0]}
        left=0
        maxi=1
        for i in range(1,len(s)):
            while(s[i] in new):
                new.remove(s[left])
                left+=1
            new.add(s[i])
            maxi=max(maxi,i-left+1)
        return maxi
