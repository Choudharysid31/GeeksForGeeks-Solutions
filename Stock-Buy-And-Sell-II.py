'''The cost of stock on each day is given in an array price[] of size n. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day, Find the maximum profit which you can get.

Note: Buying and Selling of the stock can be done multiple times, but you can only hold one stock at a time. In order to buy another stock, firstly you have to sell the current holding stock.

Example 1:

Input:
n = 4
price[] = {3, 4, 1, 5}
Output:
5
Explanation:
We can buy stock on day 1 (at price 3) and sell it on day 2 (at price 4) profit will be 4-3=1, 
We can buy another stock on day 3 (at price 1) and sell it on day 4 (at price 5) profit will be 5-1=4, 
which will give us maximum profit of 1+4=5.
Example 2:

Input:
n = 5
price[] = {1, 3, 5, 7, 9}
Output:
8
Explanation:
We can buy stock on day 1 (at price 1) and sell it on day 5 (at price 9), which will give us maximum profit of 8.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''


class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        # code here
        buy=prices[0]
        maxi=0
        for i in range(1,n):
            if buy>=prices[i] or prices[i-1]>prices[i]:
                maxi+=prices[i-1]-buy
                buy=prices[i]
        maxi+=prices[-1]-buy 
   
        return maxi
