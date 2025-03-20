'''Given a string s, count all palindromic sub-strings present in the string. The length of the palindromic sub-string must be greater than or equal to 2. 

Input: s = "abaab"
Output: 3
Explanation: All palindromic substrings are : "aba" , "aa" , "baab".

Input: s = "aaa"
Output: 3
Explanation: All palindromic substrings are : "aa", "aa", "aaa".

Input: s = "abbaeae"
Output: 4
Explanation: All palindromic substrings are : "bb" , "abba" , "aea", "eae".'''

class Solution:

    def countPS(self, s):
        count=0
        
        for i in range(len(s)):
            #odd length
            left=i-1
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1)>1:
                    count+=1
                left-=1
                right+=1

        for i in range(len(s)):
            #even length
            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1)>1:
                    count+=1
                left-=1
                right+=1
    
        return(count)
