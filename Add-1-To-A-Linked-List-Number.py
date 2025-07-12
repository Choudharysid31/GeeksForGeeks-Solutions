'''You are given a linked list where each element in the list is a node and have an integer data. You need to add 1 to the number formed by concatinating all the list node numbers together and return the head of the modified linked list. 

Input: LinkedList: 4->5->6
Output: 457

Input: LinkedList: 1->2->3
Output: 124

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''

class Solution:
    def addOne(self,head):
        
        def reverse(head):
            rev=None
            temp=head
            while temp:
                curr=temp.next
                temp.next=rev
                rev=temp
                temp=curr
            return rev
            
        head=reverse(head)
        
        sumi=head.data+1
        carry=sumi//10
        head.data=sumi%10
        temp=head.next
        
        while temp and carry:
            sumi=temp.data+carry
            temp.data=sumi%10
            carry=sumi//10
            temp=temp.next

        head=reverse(head)
            
        if carry:
            node=Node(1)
            node.next=head
            return node
            
        return head
