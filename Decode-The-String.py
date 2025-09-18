'''Given an encoded string s, decode it by expanding the pattern k[substring], where the substring inside brackets is written k times. k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets. Return the final decoded string.

Input: s = "3[b2[ca]]"
Output: "bcacabcacabcaca"
Explanation: Inner substring “2[ca]” breakdown into “caca”. Now, new string becomes “3[bcaca]”. Similarly “3[bcaca]” becomes “bcacabcacabcaca” which is final result.

Input: s = "3[ab]"
Output: "ababab"
Explanation: The substring "ab" is repeated 3 times giving "ababab".

Constraints:
1 ≤ |s| ≤ 105 
1 ≤ k ≤ 100'''

class Solution:
    def decodedString(self, s):
        # code here
        stack=[]
        
        for i in s:
            
            if i==']':
                temp=[]
                
                while stack[-1]!='[':
                    temp.append(stack.pop())
                
                stack.pop()
                temp=''.join(temp[::-1])
                
                count=''
                while stack and stack[-1].isdigit():
                    count+=stack.pop()

                temp=temp*int(count[::-1])
                stack.append(temp)
            
            else:
                stack.append(i)
                
        return ''.join(stack)
                    

