'''Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only. Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.

Input: head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2
Output: 0 → 1 → 1 → 2 → 2 → 2 → 2 → 2

Input: head = 2 → 2 → 0 → 1
Output: 0 → 1 → 2 → 2

1 ≤ no. of nodes ≤ 106
0 ≤ node->data ≤ 2'''

	
class Solution:
    def segregate(self, head):
        zeroH=Node(-1)
        oneH=Node(-1)
        twoH=Node(-1)
        
        zero=zeroH
        one=oneH
        two=twoH
        temp=head
        
        while temp:
            if temp.data==0:
                zero.next=temp
                zero=zero.next
            elif temp.data==1:
                one.next=temp
                one=one.next
            else:
                two.next=temp
                two=two.next
            temp=temp.next
            
        zero.next=oneH.next if oneH.next else twoH.next
        one.next=twoH.next
        two.next=None
            
        head=zeroH.next
        del(zeroH)
        del(oneH)
        del(twoH)
        
        return head
