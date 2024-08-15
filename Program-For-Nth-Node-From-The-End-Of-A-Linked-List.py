'''Given the head of a linked list and the number k, Your task is to find the kth node from the end. If k is more than the number of nodes, then the output should be -1.

Examples

Input: LinkedList: 1->2->3->4->5->6->7->8->9, k = 2
Output: 8
Explanation: The given linked list is 1->2->3->4->5->6->7->8->9. The 2nd node from end is 8.

Input: LinkedList: 10->5->100->5, k = 5
Output: -1
Explanation: The given linked list is 10->5->100->5. Since 'k' is more than the number of nodes, the output is -1.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).'''


class Solution:
    def getKthFromLast(self, head, k):
        temp=head
        leni=0
        while temp:
            temp=temp.next
            leni+=1
        i=leni-k
        if i<0:
            return -1
        curr=None
        temp=head
        while i+1:
            curr=temp.data
            temp=temp.next
            i-=1
        return curr
