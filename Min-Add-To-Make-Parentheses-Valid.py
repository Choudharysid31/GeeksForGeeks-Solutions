'''You are given a string s consisting only of the characters '(' and ')'. Your task is to determine the minimum number of parentheses (either '(' or ')') that must be inserted at any positions to make the string s a valid parentheses string.

Input: s = "(()("
Output: 2
Explanation: There are two unmatched '(' at the end, so we need to add two ')' to make the string valid.

Input: s = ")))"
Output: 3

Input: s = ")()()"
Output: 1 

Constraints:
1 ≤ s.size() ≤ 105
s[i] ∈ { '(' , ')' }'''

class Solution:
    def minParentheses(self, s):
        count=0
        stack=[]

        for i in s:
            if i==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    count+=1
            else:
                stack.append(i)
                
        return count+len(stack)

