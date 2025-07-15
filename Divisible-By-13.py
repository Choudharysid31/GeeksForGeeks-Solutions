'''Given a number represented as a string s (which may be very large), check whether it is divisible by 13 or not.

Input : s = "2911285"
Output : true

Input : s = "27"
Output : false

1 ≤  s.size()  ≤ 105'''

class Solution:
    def divby13(self, s):
        j=len(s)
        arr=[]
    
        while j>0:
            arr.append(int(s[max(j-3,0):j]))
            j=j-3
            
        check=1
        sume=0
        for i in arr:
            sume+=check*i
            check*=-1
        
        return True if sume%13==0 else False
