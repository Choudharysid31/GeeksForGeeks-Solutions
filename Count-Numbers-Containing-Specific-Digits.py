'''You are given an integer n representing the number of digits in a number, and an array arr[] containing digits from 0 to 9. Your have to count how many n-digit positive integers can be formed such that at least one digit from the array arr[] appears in the number.

Input: n = 1, arr[] = [1, 2, 3]
Output: 3
Explanation: Only the single-digit numbers [1, 2, 3] satisfy the condition.

Input: n = 2, arr[] = [3, 5]
Output: 34

1 ≤ n ≤ 9
1 ≤ arr.size() ≤ 10
0 ≤ arr[i] ≤ 9'''

class Solution:
    def countValid(self, n, arr):
        total_num=9*(10)**(n-1)
        m=10-len(arr)
        not_pos=m**(n-1)*(m if 0 in arr else m-1)
        
        return total_num-not_pos
