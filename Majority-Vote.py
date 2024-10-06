'''You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return -1. 
Note: The answer should be returned in an increasing format.

Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.

Input: arr[] = [1, 2, 3, 4, 5]
Output: [-1]
Explanation: no candidate occur more than n/3 times.

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)'''

class Solution:
    def findMajority(self, arr):
        if len(arr)<2:
            return [arr[0]]
        ele1=-1
        count1=0
        ele2=-1
        count2=0
        for i in range(len(arr)):
            if arr[i]==ele1:
                count1+=1
            elif arr[i]==ele2:
                count2+=1
            elif count1==0:
                ele1=arr[i]
                count1=1
            elif count2==0:
                ele2=arr[i]
                count2=1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for i in arr:
            if i==ele1:
                count1+=1
            elif i==ele2:
                count2+=1
        res=[]
        if (count1>len(arr)//3):
            res.append(ele1)
        if (count2>len(arr)//3):
            res.append(ele2)
        if len(res):
            return sorted(res)
        return [-1]
