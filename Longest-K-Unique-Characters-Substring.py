'''Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.

Example 1:
S = "aabacbebebe", K = 3
Output: 7
Explanation: "cbebebe" is the longest substring with 3 distinct characters.

Example 2:
S = "aaaa", K = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).'''
class Solution:
    def longestKSubstr(self, s, k):
        dicti={}
        longest=-1
        j=0
        i=0
        while i<len(s):
            if s[i] not in dicti:
                dicti[s[i]]=1
            else:
                dicti[s[i]]+=1
            while len(dicti)>k:
                dicti[s[j]]-=1
                if dicti[s[j]]==0:
                    del(dicti[s[j]])
                j+=1
            if len(dicti)==k:
                longest=max(longest,i-j+1)
            i+=1
        return longest
