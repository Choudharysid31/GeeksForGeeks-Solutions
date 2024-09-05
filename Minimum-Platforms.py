'''Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.
Note: Time intervals are in the 24-hour format(HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0).

Input: arr[] = [0900, 0940, 0950, 1100, 1500, 1800], 
      dep[] = [0910, 1200, 1120, 1130, 1900, 2000]
Output: 3

Explanation: There are three trains during the time 0940 to 1200. So we need minimum 3 platforms.
Input: arr[] = [0900, 1235, 1100], 
       dep[] = [1000, 1240, 1200]
Output: 1
Explanation: All train times are mutually exlusive. So we need only one platform

Expected Time Complexity: O(nLogn)
Expected Auxiliary Space: O(n)'''
    def minimumPlatform(self,arr,dep):
        arr.sort()
        dep.sort()
        i=0
        j=0
        plat=0
        ans=0
        while i<n and j<n:
            if arr[i]<=dep[j]:
                plat+=1
                i+=1
            else:
                plat-=1
                j+=1
            ans=max(ans,plat)
        return ans
