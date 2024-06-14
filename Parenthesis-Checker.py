'''Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".

Example 1:

Input:
{([])}
Output: 
true
Explanation: 
{ ( [ ] ) }. Same colored brackets can form 
balanced pairs, with 0 number of 
unbalanced bracket.'''

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        arr=[]
        if len(x)%2!=0:
            return False
        for i in x:
            if i=="{" or i=="[" or i=="(":
                arr.append(i)
            else:
                if len(arr):
                    if (i=="}"and arr[-1]=="{") or (i==")"and arr[-1]=="(") or (i=="]"and arr[-1]=="["):
                        arr.pop()
                    else:
                        return False
                else:
                    return False
        if len(arr):
            return False
        return True
