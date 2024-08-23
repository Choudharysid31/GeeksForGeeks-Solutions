'''Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. If the conversion is not feasible, the function should return -1.
Note: Conversion is feasible only if all characters in the string are numeric or if its first character is '-' and rest are numeric.

Examples:
Input: s = "-123"
Output: -123
Explanation: It is possible to convert -123 into an integer so we returned in the form of an integer

Input: s = "21a"
Output: -1
Explanation: The output is -1 as, due to the inclusion of 'a', the given string cannot be converted to an integer.

Expected Time Complexity: O( |s| ), 
Expected Auxiliary Space: O(1)'''

class Solution:
    def atoi(self,s):
        num=0
        flag=False
        if s[0]=='-':
            flag=True
            for i in s[1:]:
                if i>='0' and i<='9':
                    num=num*10+(ord(i)-ord('0'))
                else:
                    return -1
            return -num
        else:
            for i in s:
                if i>='0' and i<='9':
                    num=num*10+(ord(i)-ord('0'))
                else:
                    return -1
            return num
