'''Given two integers n and k, the task is to find all valid combinations of k numbers that adds up to n based on the following conditions:
Only numbers from the range [1, 9] used. Each number can only be used at most once.
Note: You can return the combinations in any order, the driver code will print them in sorted order.

Input: n = 9, k = 3
Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
Explanation: There are three valid combinations of 3 numbers that sum to 9: [1 ,2, 6], [1, 3, 5] and [2, 3, 4].

Input: n = 3, k = 3
Output: []
Explanation: It is not possible to pick 3 distinct numbers from 1 to 9 that sum to 3, so no valid combinations exist.

Constraints:
1 ≤ n ≤ 50
1 ≤ k ≤ 9'''

from itertools import combinations
class Solution:
    # def combinationSum(self, n, k):
        
    #     avail=[i for i in range(1,10)]
    #     return [list(arr) for arr in list(combinations(avail,k)) if sum(arr)==n]

    def backtrack(self, tot,dig,arr,ans,count):
        
        if len(arr)==count and tot==0:
            ans.append(arr[:])
        if tot<=0 or dig==0 or len(arr)>count:
            return
        arr.append(dig)
        
        self.backtrack(tot-dig,dig-1,arr,ans,count)
        arr.pop()
        self.backtrack(tot,dig-1,arr,ans,count)
        
    def combinationSum(self, n, k):
        ans=[]
        self.backtrack(n,9,[],ans,k)
        return ans
