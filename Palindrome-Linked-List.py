'''Given a singly linked list of integers. The task is to check if the given linked list is palindrome or not.
Examples:
Input: LinkedList: 1->2->1->1->2->1
Output: true
Explanation: The given linked list is 1->2->1->1->2->1 , which is a palindrome and Hence, the output is true.

Input: LinkedList: 1->2->3->4
Output: false
Explanation: The given linked list is 1->2->3->4, which is not a palindrome and Hence, the output is false.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''
class Solution:
    def isPalindrome(self, head):
        arr=[]
        temp=head
        while temp:
            arr.append(temp.data)
            temp=temp.next
        return arr==arr[::-1]
