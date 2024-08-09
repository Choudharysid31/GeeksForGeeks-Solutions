'''You are given an integer n and an integer array arr of size n+2.All elements of the array are in the range from 1 to n.Also, all elements occur once except two numbers which occur twice. Find the two repeating numbers.
Note: Return the numbers in their order of appearing twice. So, if x and y are repeating numbers, and x's second appearance comes before the second appearance of y,then the order should be (x, y).
Examples:
Input: n = 4, arr[] = [1, 2, 1, 3, 4, 3]
Output: 1 3
Explanation: In the given array, 1 and 3 are repeated two times, and as 1's second appearance occurs before 2's second appearance, so the output should be 1 3.
Input: n = 2, arr[] = [1, 2, 2, 1]
Output: 2 1
Explanation: In the given array, 1 and 2 are repeated two times and second occurence of 2 comes before 1. So the output is 2 1.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1). '''

class Solution:
    def twoRepeated(self, n, arr):
        #Your code here
        out=set()
        res=[]
        for i in arr:
            if i not in out:
                out.add(i)
            else:
                res.append(i)
        return res
