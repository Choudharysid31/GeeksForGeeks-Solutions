'''Given a singly linked list's head. Your task is to complete the function alternatingSplitList() that splits the given linked list into two smaller lists. The sublists should be made from alternating elements from the original list.

Input: LinkedList = 0->1->0->1->0->1
Output: 0->0->0 , 1->1->1
Explanation: After forming two sublists of the given list as required, we have two lists as: 0->0->0 and 1->1->1.

Input: LinkedList = 2->5->8->9->6
Output: 2->8->6 , 5->9
Explanation: After forming two sublists of the given list as required, we have two lists as: 2->8->6 and 5->9.

Input: LinkedList: 7 
Output: 7 , <empty linked list>'''

class Solution:
    def alternatingSplitList(self, head):
        if head is None:
            return (None,None)
        elif head.next is None:
            return (head,None)
        head1=head
        head2=head.next
        new1=head1
        new2=head2
        while new1 and new2:
            new1.next=new2.next
            new1=new2.next
            if new2.next:
                new2.next=new1.next
                new2=new1.next
        return head1,head2
