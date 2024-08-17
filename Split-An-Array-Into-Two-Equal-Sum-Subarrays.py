'''Given an array of integers arr, return true if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays are equal. If it is not possible then return false.

Examples:
Input: arr = [1, 2, 3, 4, 5, 5]
Output: true
Explanation: In the above example, we can divide the array into two subarrays with eqaul sum. The two subarrays are: [1, 2, 3, 4] and [5, 5]. The sum of both the subarrays are 10. Hence, the answer is true.

Input: arr = [4, 3, 2, 1]
Output: false
Explanation: In the above example, we cannot divide the array into two subarrays with eqaul sum. Hence, the answer is false.

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)'''

class Solution:
    def canSplit(self, arr):
        sume=sum(arr)
        if sume%2==1:
            return False
        front=0
        for i in range(len(arr)):
            front+=arr[i]
            if front==sume//2:
                break
        if i==len(arr)-1:
            return False
        back=0
        for j in range(len(arr)-1,-1,-1):
            back+=arr[j]
            if back==sume//2:
                break
        if j==0:
            return False
        if j-i==1:
            return True
        return False
