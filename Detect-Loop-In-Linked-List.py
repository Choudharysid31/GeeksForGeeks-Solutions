'''Given the head of a singly linked list, the task is to check if the linked list has a loop. A loop means that the last node of the linked list is connected back to a node in the same list.  So if the next of the last node is null. then there is no loop.
Note: You need to return a boolean value true if there is a loop, otherwise false.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1).'''

class Solution:

    def detectLoop(self, head):
        temp=head
        temp1=head
        while temp1 and temp1.next:
            temp=temp.next
            temp1=temp1.next.next
            if temp1==temp:
                return True

        return False
