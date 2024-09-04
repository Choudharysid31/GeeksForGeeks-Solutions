'''You are given an array of integers and a value k. The task is to find the count of all sub-arrays whose sum is divisible by k.

Input: arr[] = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
Explanation: There are 7 sub-arrays whose is divisible by k: [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3] and [-2, -3]

Input: arr[] = [2, 2, 2, 2, 2, 2], k = 2
Output: 21
Explanation: All subarray sums are divisible by 2
Expected Time Complexity: O(n+k).
Expected Auxiliary Space: O(k).'''

    def subCount(self, arr, k):
        hash1={}
        count=0
        curr=0
        for i in arr:
            curr+=i
            rem=curr%k
            if rem==0:
                count+=1
            if rem<0:
                rem+=k
            if rem in hash1:
                count+=hash1[rem]
            if rem not in hash1:
                hash1[rem]=0
            hash1[rem]+=1
        return count
