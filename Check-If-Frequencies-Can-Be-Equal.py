'''Given a string s consisting only lowercase alphabetic characters, check whether it is possible to remove at most one character such that the  frequency of each distinct character in the string becomes same. Return true if it is possible; otherwise, return false.

Input: s = "xyyz"
Output: true 
Explanation: Removing one 'y' will make frequency of each distinct character to be 1.

Input: s = "xyyzz"
Output: true
Explanation: Removing one 'x' will make frequency of each distinct character to be 2.

Input: s = "xxxxyyzz"
Output: false
Explanation: Frequency can not be made same by removing at most one character.'''

class Solution:
    def sameFreq(self, s: str) -> bool:
        
        dicti={}
        for i in s:
            dicti[i]=dicti.get(i,0)+1
            
        checker={}
        for j in dicti:
            checker[dicti[j]]=checker.get(dicti[j],0)+1
        if len(checker)>2:
            return False
        maxi=-float("inf")
        mini=float("inf")
        for key in checker:
            mini=min(key,mini)
            maxi=max(key,maxi)

        if (maxi-mini)>1:
            if (mini==1 and checker[mini]==1):
                return True
            return False
        if (checker[mini]<checker[maxi] and mini!=1):
            return False
        if (len(checker)>1 and checker[mini]!=1 and checker[maxi]!=1):
            return False
            

        return True
