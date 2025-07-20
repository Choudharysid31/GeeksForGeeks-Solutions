''' Given a maze with n cells. Each cell may have multiple entry points but not more than one exit point (i.e entry/exit points are unidirectional doors like valves).You are given an array exits[], where exits[i] contains the exit point of the ith cell.
If exits[i] is -1, then ith cell doesn't have an exit.

The task is to find the cell with maximum weight (The weight of a cell i is the sum of all the cell indexes that have exit point as i ). If there are multiple cells with the maximum weight return the cell with highest index.

Note: The cells are indexed with an integer value from 0 to n-1.
A cell i has weight 0 if no cell has exit point as i.

Input: exits[] = [2, 0, -1, 2}
Output: 2
Explanation: 
1 -> 0 -> 2 <- 3
weight of 0th cell = 1
weight of 1st cell = 0 (because there is no cell pointing to the 1st cell)
weight of 2nd cell = 0+3 = 3
weight of 3rd cell = 0
There is only one cell which has maximum weight (i.e 2)
So, cell 2 is the output.

Input: exits[] = [-1]
Output: 0 

1  ≤  n  ≤  105
-1  <  exits[i]  <  N
exits[i]  ≠  i'''

class Solution():
    def maxWeightCell(self, exits):
        
        ans=[0]*len(exits)
        
        for i in range(len(exits)):
            if exits[i]!=-1:
                ans[exits[i]]+=i
        
        res=0   
        idx=0
        for i in range(len(ans)):
            if res<=ans[i]:
                res=ans[i]
                idx=i
                
        return idx
