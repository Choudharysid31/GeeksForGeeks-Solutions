'''Given a string s, remove all its adjacent duplicate characters recursively. 

Example 1:
S = "geeksforgeek"
Output: "gksforgk"
Explanation: g(ee)ksforg(ee)k -> gksforgk

Example 2:
S = "abccbccba"
Output: ""
Explanation: ab(cc)b(cc)ba->abbba->a(bbb)a->aa->(aa)->""(empty string)

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)'''

class Solution:
    def rremove (self, S):
        while True:
            new=''
            flag=False
            i=0
            while i<(len(S)-1):
                if S[i]!=S[i+1]:
                    new+=S[i]
                else:
                    flag=True
                    while i!=(len(S)-1) and S[i]==S[i+1]:
                        i+=1
                i+=1
            if i==len(S)-1:
                new+=S[i]
            if not flag:
                return new
            S=new
