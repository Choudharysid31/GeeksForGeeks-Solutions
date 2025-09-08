'''You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head.

Output: 5 <-> 4 <-> 3
Explanation: After reversing the given doubly linked list the new list will be 5 <-> 4 <-> 3.

Output: 196 <-> 59 <-> 122 <-> 75
Explanation: After reversing the given doubly linked list the new list will be 196 <-> 59 <-> 122 <-> 75.
   
Constraints:
1 ≤ number of nodes ≤ 106
0 ≤ node->data ≤ 104'''

class Solution:
    def reverse(self, head):
        # code here
        curr=head
        
        while curr is not None:
            
            temp=curr.next
            curr.next=curr.prev
            curr.prev=temp
            
            if temp is None:
                break
            curr=temp
            
        return curr
