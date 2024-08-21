'''Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.
Note : When you return '$' driver code will output -1.

Examples:
Input:
s = hello
Output: h
Explanation: In the given string, the first character which is non-repeating is h, as it appears first and there is no other 'h' in the string.
Input:
s = zxvczbtxyzvy
Output: c
Explanation: In the given string, 'c' is the character which is non-repeating. 

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(Number of distinct characters).'''

class Solution:

    def nonrepeatingCharacter(self,s):
        dicit={}
        for i in s:
            if i in dicit:
                dicit[i]+=1
            else:
                dicit[i]=1
        for i in s:
            if dicit[i]==1:
                return i
        return "$"
 
