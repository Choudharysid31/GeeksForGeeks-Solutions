'''Given a Binary Tree, your task is to return its In-Order Traversal.
An inorder traversal first visits the left child (including its entire subtree), then visits the node, and finally visits the right child (including its entire subtree).
Follow Up: Try solving this with O(1) auxiliary space.

Input: root[] = [1, 2, 3, 4, 5]   
Output: [4, 2, 5, 1, 3]

Input: root[] = [8, 1, 5, N, 7, 10, 6, N, 10, 6]     
Output: [1, 7, 10, 8, 6, 10, 5, 6]'''

class Solution:
    def inOrder(self,root):
        def order(node):
            if node is None:
                return
            
            order(node.left)
            
            print(node.data, end=' ')
            
            order(node.right)
            
        order(root)
        return []

