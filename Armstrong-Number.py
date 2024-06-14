'''An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 

Note: Return "true" if it is an Armstrong number else return "false".

Examples

Input: n = 153
Output: true
Explanation: 153 is an Armstrong number since 1^3 + 5^3 + 3^3 = 153. Hence answer is "true".'''


class Solution:
    def armstrongNumber (self, n):
        m=len(str(n))
        k=n
        j=0
        while n>0:
            j=j+(n%10)**m
            n=n//10
        if j==k:
            return "true"
        return "false"
