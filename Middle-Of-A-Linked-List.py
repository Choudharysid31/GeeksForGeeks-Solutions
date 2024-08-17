'''Given the head of a linked list, the task is to find the middle. For example, the middle of 1-> 2->3->4->5 is 3. If there are two middle nodes (even count), return the second middle. For example, middle of 1->2->3->4->5->6 is 4.

Examples:

Input: Linked list: 1->2->3->4->5
Output: 3
Explanation: The given linked list is 1->2->3->4->5 and its middle is 3.

Input: Linked list: 2->4->6->7->5->1
Output: 7 
Explanation: The given linked list is 2->4->6->7->5->1 and its middle is 7.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)'''

class Solution:
    def findMid(self, head):
        if head is None:
            return -1
        leni=0
        temp=head
        while temp is not None:
            leni+=1
            temp=temp.next
        leni//=2
        temp=head
        while (leni):
            temp=temp.next
            leni-=1
        return temp.data
