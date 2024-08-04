'''Given an array arr of non-negative numbers. The task is to find the first equilibrium point in an array. The equilibrium point in an array is an index (or position) such that
the sum of all elements before that index is the same as the sum of elements after it.
Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

Examples:
Input: arr[] = [1, 3, 5, 2, 2]
Output: 3 
Explanation: The equilibrium point is at position 3 as the sum of elements before it (1+3) = sum of elements after it (2+2). 
Input: arr[] = [1]
Output: 1
Explanation: Since there's only one element hence it's only the equilibrium point.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''

    def equilibriumPoint(self,arr):
        sume=sum(arr)
        new=0
        for i in range(len(arr)):
            if new==(sume-arr[i])//2:
                return i+1
            new+=arr[i]
        return -1
