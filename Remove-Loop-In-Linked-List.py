'''Given the head of a linked list that may contain a loop.  A loop means that the last node of the linked list is connected back to a node in the same list.  So if the next of the previous node is null. then there is no loop.  Remove the loop from the linked list, if it is present (we mainly need to make the next of the last node null). Otherwise, keep the linked list as it is.
The generated output will be true if your submitted code is correct, otherwise, false.

Input: Linked list: 1->3->4
Output: true

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)'''

class Solution:
    def removeLoop(self, head):
        slow=head
        fast=head
        flag=0
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                flag=1
                break
        if not flag:
            return head
        slow=head
        while slow !=fast:
            slow=slow.next
            fast=fast.next
        while fast.next!=slow:
            fast=fast.next
        fast.next=None
        return head

