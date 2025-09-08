'''Given an array arr[] of positive integers and an integer k. You have to find the sum of the modes of all the subarrays of size k.
Note: The mode of a subarray is the element that occurs with the highest frequency. If multiple elements have the same highest frequency, the smallest such element is considered the mode.

Input: arr[] = [1, 2, 3, 2, 5, 2, 4, 4], k = 3
Output: 13
Explanation: The mode of each k size subarray is [1, 2, 2, 2, 2, 4] and sum of all modes is 13.

Input: arr[] = [1, 2, 1, 3, 5], k = 2
Output: 6
Explanation: The mode of each k size subarray is [1, 1, 1, 3] and sum of all modes is 6.

Constraints:
1 ≤ k ≤ arr.size() ≤105
1 ≤ arr[i] ≤ 105'''

import heapq

class Solution:
    def sumOfModes(self, arr, k):
        
        pq=[]
        dicti={}
        start=0
        ans=0
        
        for i in range(len(arr)):
            
            dicti[arr[i]]=dicti.get(arr[i],0)+1
            heapq.heappush(pq,(-dicti[arr[i]],arr[i]))
            
            if i-start+1==k:
                
                while pq:
                    key=pq[0][1]
                    val=-pq[0][0]
                    if dicti.get(key,0)==val:
                        break
                    heapq.heappop(pq)
                    
                ans+=pq[0][1]
                
                dicti[arr[start]]-=1
                
                if dicti[arr[start]]>0:
                    heapq.heappush(pq,(-dicti[arr[start]],arr[start]))
                
                start+=1
                
        return ans

