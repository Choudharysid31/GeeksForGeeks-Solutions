'''Given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the modified Linked List.

Examples :
Input: LinkedList: 1->2->3->4->5 , x = 6
Output: 1->2->3->4->5->6
Explanation: 
We can see that 6 is inserted at the end of the linkedlist.

Input: LinkedList: 5->4 , x = 1
Output: 5->4->1
Explanation: 
We can see that 1 is inserted at the end of the linkedlist.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''

class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        new_node = Node(x)
        if head==None:
            return new_node
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        return head
