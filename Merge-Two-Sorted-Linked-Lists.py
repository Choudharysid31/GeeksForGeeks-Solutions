'''Given the head of two sorted linked lists consisting of nodes respectively. The task is to merge both lists and return the head of the sorted merged list.

Input: head1 = 5 -> 10 -> 15 -> 40, head2 = 2 -> 3 -> 20
Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40

Input: head1 = 1 -> 1, head2 = 2 -> 4
Output: 1 -> 1 -> 2 -> 4'''

class Solution:
    def sortedMerge(self,head1, head2):
        new_node=Node(-1)
        temp=new_node
        curr1=head1
        curr2=head2
        while curr1 and curr2:
            if curr1.data<=curr2.data:
                temp.next=curr1
                curr1=curr1.next
                temp=temp.next
            else:
                temp.next=curr2
                curr2=curr2.next
                temp=temp.next
        while curr1:
            temp.next=curr1
            curr1=curr1.next
            temp=temp.next
        while curr2:
            temp.next=curr2
            curr2=curr2.next
            temp=temp.next
        return new_node.next

