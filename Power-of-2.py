'''Given a non-negative integer n. The task is to check if it is a power of 2. 
Examples
Input: n = 8
Output: true
Explanation: 8 is equal to 2 raised to 3 (2^3 = 8).
Input: n = 98
Output: false
Explanation: 98 cannot be obtained by any power of 2.'''

    def isPowerofTwo(self,n : int ) -> bool:
        n=bin(n)[2:]
        for i in range(1,len(n)):
            if n[i]=='1':
                return False
        if n[0]=="0":
            return False
        return True
