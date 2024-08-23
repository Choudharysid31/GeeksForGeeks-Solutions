'''Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
I 1, V 5, X 10, L 50, C 100, D 500, M 1000

Example 1:
s = V
Output: 5

Example 2:
Input:
s = III 

Expected Time Complexity: O(|S|), |S| = length of string S.
Expected Auxiliary Space: O(1)'''

class Solution:
    def romanToDecimal(self, S): 
        val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        for i in range(len(S)-1):
            if val[S[i]]>=val[S[i+1]]:
                num+=val[S[i]]
            else:
                num-=val[S[i]]
        return num+val[S[-1]]
