'''Given the head a linked list, the task is to reverse every k node in the linked list. If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed.

Input: head = 1 -> 2 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8, k = 4
Output: 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5
Explanation: The first 4 elements 1, 2, 2, 4 are reversed first and then next 4 elements 5, 6, 7, 8. Hence, the resultant linked list is 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5.

Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 3
Output: 3 -> 2 -> 1 -> 5 -> 4
Explanation: The first 3 elements 1, 2, 3 are reversed first and then left out elements 4, 5 are reversed. Hence, the resultant linked list is 3 -> 2 -> 1 -> 5 -> 4.'''

class Solution:
    def reverseKGroup(self, head, k):
        m=k        
        rev=None
        temp=head
        flag=False
        while k>0 and temp:
            curr=temp.next
            temp.next=rev
            rev=temp
            temp=curr
            k-=1
            if k==0:
                if not flag:
                    new_head=rev
                    flag=True
                else:
                    head.next=rev
                    head=curr_head
                curr_head=curr
                rev=None
                k=m
        if k!=m:
            head.next=rev
        return new_head
