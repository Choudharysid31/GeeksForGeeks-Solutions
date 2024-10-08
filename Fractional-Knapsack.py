'''Given weights and values of n items, we need to put these items in a knapsack of capacity w to get the maximum total value in the knapsack. Return a double value representing the maximum value in knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item here. The details of structure/class is defined in the comments above the given function.

Input: n = 3, w = 50, value[] = [60,100,120], weight[] = [10,20,30]
Output: 240.000000
Explanation: Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total value becomes 60+100+80.0=240.0 Thus, total maximum value of item we can have is 240.00 from the given capacity of sack. 

Input: n = 2, w = 50, value[] = [60,100], weight[] = [10,20]
Output: 160.000000
Explanation: Take both the items completely, without breaking. Total maximum value of item we can have is 160.00 from the given capacity of sack.

Expected Time Complexity : O(n log n)
Expected Auxilliary Space: O(1)'''

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    def fractionalknapsack(self, w,arr,n):
        val=[]
        for i in range(n):
            val.append([arr[i].value/arr[i].weight,arr[i].weight])
        val.sort(reverse=True)
        ans=0
        for i in range(n):
            if val[i][1]<=w:
                ans+=val[i][1]*val[i][0]
                w-=val[i][1]
            else:
                ans+=val[i][0]*w
                break
        return ans
