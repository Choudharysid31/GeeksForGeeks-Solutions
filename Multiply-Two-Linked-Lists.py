'''Given elements as nodes of the two singly linked lists. The task is to multiply these two linked lists, say L1 and L2.
Note: The output could be large take modulo 10^9+7.

Input: LinkedList L1 : 3->2 , LinkedList L2 : 2
Output: 64
Explanation: Multiplication of 32 and 2 gives 64.

Input: LinkedList L1: 1->0->0 , LinkedList L2 : 1->0
Output: 1000
Explanation: Multiplication of 100 and 10 gives 1000.

Expected Time Complexity: O(max(n,m))
Expected Auxilliary Space: O(1)  where n is the size of L1 and m is the size of L2'''

class Solution:
    def multiply_two_lists(self, first, second):
        num1=0
        temp1=first
        while temp1:
            num1=(num1*10+(temp1.data))%int(1e9+7)
            temp1=temp1.next
        num2=0
        temp2=second
        while temp2:
            num2=(num2*10+(temp2.data))%int(1e9+7)
            temp2=temp2.next
        
        return (num1*num2)%int(1e9+7)
