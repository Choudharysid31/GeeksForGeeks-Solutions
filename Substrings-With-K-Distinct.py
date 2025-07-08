'''Given a string consisting of lowercase characters and an integer k, the task is to count all possible substrings (not necessarily distinct) that have exactly k distinct characters. 

Input: s = "abc", k = 2
Output: 2
Explanation: Possible substrings are ["ab", "bc"]

Input: s = "aba", k = 2
Output: 3
Explanation: Possible substrings are ["ab", "ba", "aba"]

Input: s = "aa", k = 1
Output: 3
Explanation: Possible substrings are ["a", "a", "aa"]

1 ≤ s.size() ≤ 106
1 ≤ k ≤ 26'''

class Solution:
    
    def countSubstr (self, s, k):
        return self.countuptoK(s,k)-self.countuptoK(s,k-1)
        
    def countuptoK(self,s,k):
        left=0
        right=0
        checker={}
        count=0
        n=len(s)
        while right<n:
            
            checker[s[right]]=checker.get(s[right],0)+1

            while len(checker)>k:

                checker[s[left]]-=1
                if checker[s[left]]==0:
                    del(checker[s[left]])
                left+=1
                
            count+=(right-left+1)
            right+=1

        return count

