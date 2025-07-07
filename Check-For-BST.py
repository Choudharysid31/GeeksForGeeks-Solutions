'''Given the root of a binary tree. Check whether it is a BST or not. We are considering that BSTs can not contain duplicate Nodes. A BST is defined as follows:

Input: root = [2, 1, 3, N, N, N, 5]
Output: true
Explanation: The left subtree of every node contains smaller keys and right subtree of every node contains greater keys.

Input: root = [2, N, 7, N, 6, N, 9] 
Output: false
Explanation: Since the node to the right of node with key 7 has lesser key value, hence it is not a valid BST.

Input: root = [10, 5, 20, N, N, 9, 25]
Output: false
Explanation: The node with key 9 present in the right subtree has lesser key value than root node.

1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 109'''

class Solution:
  
    def inorder(self,root,ans):
        if root is None:
            return
        self.inorder(root.left,ans)
        ans.append(root.data)
        self.inorder(root.right,ans)
      
    def isBST(self, root):
        ans=[]
        self.inorder(root,ans)
        for i in range(len(ans)-1):
            if ans[i]>=ans[i+1]:
                return False
        return True
