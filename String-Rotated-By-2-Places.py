'''Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating (in any direction) string 'a' by exactly 2 places.

Example 1:
a = amazon
b = azonam
Output: 1
Explanation: amazon can be rotated anti-clockwise by two places, which will make it as azonam.

Example 2:
a = geeksforgeeks
b = geeksgeeksfor
Output: 0
Explanation: If we rotate geeksforgeeks by two place in any direction, we won't get geeksgeeksfor.'''

class Solution:
    def isRotated(self,str1,str2):
        if (str1[2:]==str2[:len(str2)-2]) and (str1[:2]==str2[len(str2)-2:]):
            return 1
        if (str1[len(str1)-2:]==str2[:2]) and (str1[:len(str1)-2]==str2[2:]):
            return 1
        return 0
