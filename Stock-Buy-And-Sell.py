'''The cost of stock on each day is given in an array A[] of size N. Find all the segments of days on which you buy and sell the stock such that the sum of difference between sell and buy prices is maximized. Each segment consists of indexes of two elements, first is index of day on which you buy stock and second is index of day on which you sell stock.
Note: Since there can be multiple solutions, the driver code will print 1 if your answer is correct, otherwise, it will return 0. In case there's no profit the driver code will print the string "No Profit" for a correct solution.

Example 1:
Input:
N = 7
A[] = {100,180,260,310,40,535,695}
Output:
1
Explanation:One possible solution is (0 3) (4 6)We can buy stock on day 0,and sell it on 3rd day, which will give us maximum profit. Now, we buy stock on day 4 and sell it on day 6.

Example 2:
Input:
N = 5
A[] = {4,2,2,2,4}
Output:
1
Explanation: There are multiple possible solutions.one of them is (3 4)We can buy stock on day 3,and sell it on 4th day, which will give us maximum profit.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)'''


class Solution:
	def stockBuySell(self, A, n):

		buy=A[0]
		maxi=0
		buy_index=0
    ans=[]

        for i in range(1,n):

            if buy>=A[i] or A[i-1]>A[i]:

                maxi+=A[i-1]-buy

                if maxi:

                    ans.append([buy_index,i-1])

                buy=A[i]

                buy_index=i

                maxi=0

        maxi+=A[-1]-buy

        if maxi:

            ans.append([buy_index,n-1])

        return ans

