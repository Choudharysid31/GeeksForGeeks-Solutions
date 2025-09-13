'''Given a board of dimensions n × m that needs to be cut into n*m squares. The cost of making a cut along a horizontal or vertical edge is provided in two arrays:

x[]: Cutting costs along the vertical edges (length-wise).
y[]: Cutting costs along the horizontal edges (width-wise).
Find the minimum total cost required to cut the board into squares optimally.

Examples:

Input: n = 4, m = 6, x[] = [2, 1, 3, 1, 4], y[] = [4, 1, 2]
Output: 42

Initially no. of horizontal segments = 1 & no. of vertical segments = 1.
Optimal way to cut into square is:
• Pick 4 (from x) -> vertical cut, Cost = 4 × horizontal segments = 4,
  Now, horizontal segments = 1, vertical segments = 2.
• Pick 4 (from y) -> horizontal cut, Cost = 4 × vertical segments = 8,
  Now, horizontal segments = 2, vertical segments = 2.
• Pick 3 (from x) -> vertical cut, Cost = 3 × horizontal segments = 6,
  Now, horizontal segments = 2, vertical segments = 3.
• Pick 2 (from x) -> vertical cut, Cost = 2 × horizontal segments = 4,
  Now, horizontal segments = 2, vertical segments = 4.
• Pick 2 (from y) -> horizontal cut, Cost = 2 × vertical segments = 8,
  Now, horizontal segments = 3, vertical segments = 4.
• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 3,
  Now, horizontal segments = 3, vertical segments = 5.
• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 3,
  Now, horizontal segments = 3, vertical segments = 6.
• Pick 1 (from y) -> horizontal cut, Cost = 1 × vertical segments = 6,
  Now, horizontal segments = 4, vertical segments = 6.
So, the total cost = 4 + 8 + 6 + 4 + 8 + 3 + 3 + 6 = 42.

Input: n = 4, m = 4, x[] = [1, 1, 1], y[] = [1, 1, 1]
Output: 15

Constraint:
2 ≤ n, m ≤ 103
1 ≤ x[i], y[j] ≤103'''

class Solution:
    def minCost(self, n, m, x, y):
        hoz=1
        vert=1
        
        x.sort()
        y.sort()
        
        len_x=len(x)-1
        len_y=len(y)-1
        ans=0
        while (len_x>=0 and len_y>=0):
            if (x[len_x]>y[len_y]):
                ans+=x[len_x]*hoz
                vert+=1
                len_x-=1
            else:
                ans+=y[len_y]*vert
                hoz+=1
                len_y-=1
                
        while len_x>=0:
            ans+=x[len_x]*hoz
            len_x-=1
        
        while len_y>=0:
            ans+=y[len_y]*vert
            hoz+=1
            len_y-=1            
        
        return ans
