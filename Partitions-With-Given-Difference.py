'''Given an array arr, partition it into two subsets(possibly empty) such that each element must belong to only one subset. Let the sum of the elements of these two subsets be S1 and S2. Given a difference d, count the number of partitions in which S1 is greater than or equal to S2 and the difference between S1 and S2 is equal to d. Since the answer may be large return it modulo 109 + 7.

Input: n = 4 d = 3 arr[] =  { 5, 2, 6, 4}
Output: 1
Explanation:There is only one possible partition of this array. Partition : {6, 4}, {5, 2}. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3.

Input: n = 4 d = 0 arr[] = {1, 1, 1, 1} 
Output: 6 
Explanation: we can choose two 1's from indices {0,1}, {0,2}, {0,3}, {1,2}, {1,3}, {2,3} and put them in S1 and remaning two 1's in S2.
Thus there are total 6 ways for partition the array arr. 

Expected Time Complexity: O( n*sum(arr))
Expected Space Complexity: O( sum(arr))'''

class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        target=sum(arr)
        if (target-d)<0 or (target-d)%2!=0:
            return 0
        target=(target-d)//2

        dp=[[0]*(target+1) for _ in range(n+1)]
        for i in range(n):
		    dp[i][0]=1
		for i in range(1,target+1):
		    dp[0][i]=0
        for i in range(1,n+1):
            for j in range(target+1):
                if arr[i-1]>j:
                    dp[i][j]=(dp[i-1][j])
                else:
                    dp[i][j]=(dp[i-1][j] + dp[i-1][j-arr[i-1]])%1000000007
                    
        return dp[n][target]%1000000007
