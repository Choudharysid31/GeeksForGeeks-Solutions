'''Given two numbers as strings s1 and s2. Calculate their Product.
Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.

Example 1:
s1 = "0033"
s2 = "2"
Output: 66

Example 2:
s1 = "11"
s2 = "23"
Output:253

Expected Time Complexity: O(n1* n2)
Expected Auxiliary Space: O(n1 + n2); where n1 and n2 are sizes of strings s1 and s2 respectively.'''

class Solution:
    def multiplyStrings(self,s1,s2):
        num1=0
        if s1[0]=='-':
            for i in s1[1:]:
                num1=num1*10+(ord(i)-ord('0'))
            num1=-num1
        else:
            for i in s1:
                num1=num1*10+(ord(i)-ord('0'))
        num2=0
        if s2[0]=='-':
            for i in s2[1:]:
                num2=num2*10+(ord(i)-ord('0'))
            num2=-num2
        else:
            for i in s2:
                num2=num2*10+(ord(i)-ord('0'))
        return num2*num1
        
