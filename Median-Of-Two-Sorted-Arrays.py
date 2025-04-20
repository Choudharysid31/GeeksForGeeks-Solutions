''' Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        j=0
        i=0
        med1=0
        med2=0
  
        while ((i+j)<((n+m)//2)+1 and i<n and j<m):
            if nums1[i] < nums2[j]:
                med2=med1
                med1=nums1[i]
                i+=1
            else:
                med2=med1
                med1=nums2[j]
                j+=1
              
        while ((i+j)<((n+m)//2)+1 and i<n):
            med2=med1
            med1=nums1[i]
            i+=1
          
        while ((i+j)<((n+m)//2)+1 and j<m):
            med2=med1
            med1=nums2[j]
            j+=1
          
        if (n+m)%2==0:
            return (med1+med2)/2
          
        return med1
