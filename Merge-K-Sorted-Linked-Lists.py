''' Given an array arr[] of n sorted linked lists of different sizes. Your task is to merge all these lists into a single sorted linked list and return the head of the merged list.

Output: 1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9
Explanation: The arr[] has 3 sorted linked list of size 3, 3, 1.
1st list: 1 -> 3 -> 7
2nd list: 2 -> 4 -> 8
3rd list: 9
    
Output: 1 -> 3 -> 4 -> 5 -> 6 -> 8
Explanation: The arr[] has 3 sorted linked list of size 2, 1, 3.
1st list: 1 -> 3
2nd list: 8
3rd list: 4 -> 5 -> 6
The merged list will be: 
    
Constraints
1 ≤ total no. of nodes ≤ 105
1 ≤ node->data ≤ 103'''

import heapq

class Solution:
    def mergeKLists(self, arr):
        # code here
        check=[]
        new_head=Node(-1)
        tail=new_head
        for i in range(len(arr)):
            head=arr[i]
            if head is not None:
                heapq.heappush(check,(head.data,head))
        while check:
            
            data,node=heapq.heappop(check)
            
            tail.next=node
            tail=tail.next
            
            if tail.next is not None:
                heapq.heappush(check,(tail.next.data,tail.next))
            
        return new_head.next
