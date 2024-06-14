''' Given an array of size n-1 such that it only contains distinct integers in the range of 1 to n. Return the missing element.

Examples:

Input: n = 5, arr[] = {1,2,3,5}
Output: 4
Explanation : All the numbers from 1 to 5 are present except 4.
Input: n = 2, arr[] = {1}
Output: 2
Explanation : All the numbers from 1 to 2 are present except 2.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 10^6
1 ≤ arr[i] ≤ 10^6 '''

class Solution:
    def missingNumber(self,array,n):
        sum1=0
        for i in array:
            sum1+=i
        return int(n*(n+1)/2) - (sum1)


