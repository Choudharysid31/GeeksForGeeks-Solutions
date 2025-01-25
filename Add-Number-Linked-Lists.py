'''Given the head of two singly linked lists num1 and num2 representing two non-negative integers. The task is to return the head of the linked list representing the sum of these two numbers. For example, num1 represented by the linked list : 1 -> 9 -> 0, similarly num2 represented by the linked list: 2 -> 5. Sum of these two numbers is represented by 2 -> 1 -> 5.
Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

Input: num1 = 4 - > 5, num2 = 3 -> 4 -> 5
Output:  3 -> 9 -> 0
Explanation: Given numbers are 45 and 345. There sum is 390.

Input: num1 = 0 -> 0 -> 6 -> 3, num2 = 0 -> 7 
Output: 7 -> 0 
Explanation: Given numbers are 63 and 7. There sum is 70.'''

class Solution:
    def addTwoLists(self, num1, num2):
        
        temp=num1
        rev1=None
        
        while temp:
            curr=temp.next
            temp.next=rev1
            rev1=temp
            temp=curr
            
        temp=num2
        rev2=None
        
        while temp:
            curr=temp.next
            temp.next=rev2
            rev2=temp
            temp=curr
            
        temp1=rev1
        temp2=rev2
        val=(temp1.data+temp2.data)%10
        carry=(temp1.data+temp2.data)//10
        new_node=Node(val)
        temp=new_node
        
        while temp1.next and temp2.next:
            temp1=temp1.next
            temp2=temp2.next
            val=(temp1.data+temp2.data+carry)%10
            carry=(temp1.data+temp2.data+carry)//10
            temp.next=Node(val)
            temp=temp.next
        
        while temp1.next:
            temp1=temp1.next
            val=(temp1.data+carry)%10
            carry=(temp1.data+carry)//10
            temp.next=Node(val)
            temp=temp.next
        
        while temp2.next:
            temp2=temp2.next
            val=(temp2.data+carry)%10
            carry=(temp2.data+carry)//10
            temp.next=Node(val)
            temp=temp.next
        
        if carry==1:
            temp.next=Node(1)
            temp=temp.next
        
        temp.next=None
        temp=new_node
        rev=None
        
        while temp:
            curr=temp.next
            temp.next=rev
            rev=temp
            temp=curr
        
        while rev.data==0:
            rev=rev.next
        
        return rev


