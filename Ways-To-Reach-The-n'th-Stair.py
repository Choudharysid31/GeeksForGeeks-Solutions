'''There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top (order does matter).
Note:  Returns the answer % 10^9+7.

Input: n = 4
Output: 5
Explanation: You can reach 4th stair in 5 ways. 
Way 1: Climb 2 stairs at a time. 
Way 2: Climb 1 stair at a time.
Way 3: Climb 2 stairs, then 1 stair and then 1 stair.
Way 4: Climb 1 stair, then 2 stairs then 1 stair.
Way 5: Climb 1 stair, then 1 stair and then 2 stairs.

Input: n = 10
Output: 89 
Explanation: There are 89 ways to reach the 10th stair.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''

    def countWays(self,n):
        arr=[0]*(n+1)
        if n<=2:
            return n
        arr[1]=1
        arr[2]=2
        for i in range(3,n+1):
            arr[i]=(arr[i-1]+arr[i-2])%1000000007
        return arr[-1]
