'''Given an array arr[] and an integer k, divide the array into k contiguous subarrays such that the maximum sum among these subarrays is minimized. 
Find this minimum possible maximum sum.

Input: arr[] = [1, 2, 3, 4], k = 3
Output: 4
Explanation: Optimal Split is [1, 2], [3], [4]. Maximum sum of all subarrays is 4, which is minimum possible for 3 splits.

Input: arr[] = [1, 1, 2], k = 2
Output: 2
Explanation: Splitting the array as [1, 1] and [2] is optimal. This results in a maximum sum subarray of 2.

1 ≤ k ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104'''

class Solution:
    def possible(self,arr,k,mid):
        presum=0
        count=1
        for ele in arr:
            presum+=ele
            if presum>mid:
                count+=1
                presum=ele
        return count<=k
    
    def splitArray(self, arr, k):
        
        left=max(arr)
        right=sum(arr)
        while left<right:
            mid=left+ (right-left)//2
            
            if self.possible(arr,k,mid):
                right=mid
            else:
                left=mid+1

                
        return left

