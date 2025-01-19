'''Given the head of a singly linked list, your task is to left rotate the linked list k times.

Input: head = 10 -> 20 -> 30 -> 40 -> 50, k = 4
Output: 50 -> 10 -> 20 -> 30 -> 40

Input: head = 10 -> 20 -> 30 -> 40 , k = 6
Output: 30 -> 40 -> 10 -> 20 '''

class Solution:
    def rotate(self, head, k):
        temp=head
        count=1
        while temp.next:
            temp=temp.next
            count+=1
        k=k%count
        if k==0:
            return head
        temp.next=head
        temp=head
        while k>1:
            temp=temp.next
            k-=1
        new_head=temp.next
        temp.next=None
        return new_head
