'''Given an integer array arr[]. Find the contiguous sub-array(containing at least one number) that has the maximum sum and return its sum.
Examples:

Input: arr[] = [1, 2, 3, -2, 5]
Output: 9
Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.
Input: arr[] = [-1, -2, -3, -4]
Output: -1
Explanation: Max subarray sum is -1 of element (-1)
Input: arr[] = [5, 4, 7]
Output: 16
Explanation: Max subarray sum is 16 of element (5, 4, 7)
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''

    def maxSubArraySum(self,arr):
        curr_sum=0
        max_sum=-float('inf')
        for i in arr:
            curr_sum=curr_sum+i
            max_sum=max(curr_sum,max_sum)
            if curr_sum<0:
                curr_sum=0
        return max_sum
