'''Given a binary string s and two integers x and y. Arrange the given string in such a way so that '0' comes X-times then '1' comes Y-times and so on until one of the '0' or '1' is finished. Then concatenate the rest of the string and find the final string.

Example 1:
X = 1, Y = 1, S = "0011"
Output: "0101"
Explanation: we put 1 '0' and 1 '1' alternatively.
Example 2:
X = 1, Y = 1, S = "1011011"
Output: "0101111"
Explanation: We put '0' and '1' alternatively and in last we have to put all '1' as there is no '0' left.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)'''

class Solution:
    def arrangeString(self, s, x, y):
        s=list(s)
        count0,count1=s.count('0'),s.count('1')
        s=''
        while count0>0 and count1>0:
            s=s+"0"*min(x,count0)
            count0-=x
            s=s+"1"*min(y,count1)
            count1-=y
        s=s+'0'*count0 +'1'*count1
        return s
