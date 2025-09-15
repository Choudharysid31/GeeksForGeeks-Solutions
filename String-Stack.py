'''You are given two strings pat and tar consisting of lowercase English characters. You can construct a new string s by performing any one of the following operation for each character in pat:
Append the character pat[i] to the string s.
Delete the last character of s (if s is empty do nothing).

After performing operations on every character of pat exactly once, your goal is to determine if it is possible to make the string s equal to string tar.

Examples:

Input: pat = "geuaek", tar = "geek"
Output: true
Explanation: Append the first three characters of pat to s, resulting in s = "geu". Delete the last character for 'a', leaving s = "ge". Then, append the last two characters 'e' and 'k' from pat to s, resulting in s = "geek", which matches tar.

Input: pat = "agiffghd", tar = "gfg"
Output: true
Explanation: Skip the first character 'a' in pat. Append 'g' and 'i' to s, resulting in s = "gi". Delete the last character for 'f', leaving s = "g". Append 'f', 'g', and 'h' to s, resulting in s = "gfgh". Finally, delete the last character for 'd', leaving s = "gfg", which matches tar.

Constraints:
1 ≤ pat.size(), tar.size() ≤ 105'''

class Solution:
    def stringStack(self, pat, tar):
        s=[]
        size=len(pat)-1
        size1=len(tar)-1

        while size>=0 and size1>=0:
  
            if pat[size]==tar[size1]:
                s.append(pat[size])
                size-=1
                size1-=1
            else:
                size-=2

        s="".join(s[::-1])

        return s==tar
        
