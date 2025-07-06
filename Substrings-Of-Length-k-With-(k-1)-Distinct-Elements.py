'''Given a string s consisting only lowercase alphabets and an integer k. Find the count of all substrings of length k which have exactly k-1 distinct characters.
Input: s = "abcc", k = 2
Output: 1

Explaination: Possible substring of length k = 2 are,
ab : 2 distinct characters
bc : 2 distinct characters
cc : 1 distinct characters

Only one valid substring so, count is equal to 1.

Input: "aabab", k = 3
Output: 3

1 ≤ s.size() ≤ 105
2 ≤ k ≤ 27'''

class Solution:
    def substrCount(self, s, k):
        count=0
        left=0
        right=1
        checker={s[0]:1}
        
        while right<len(s):
            checker[s[right]]=checker.get(s[right],0)+1
            
            if len(checker)>(k-1):
                checker[s[left]]-=1
                if checker[s[left]]==0:
                    del(checker[s[left]])
                left+=1
            if (right-left+1)>k:
                checker[s[left]]-=1
                if checker[s[left]]==0:
                    del(checker[s[left]])
                left+=1

            if len(checker)==k-1 and (right-left+1)==k:
                count+=1
                
            right+=1
        return count
