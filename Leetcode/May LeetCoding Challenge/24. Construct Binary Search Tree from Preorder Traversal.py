"""
Construct Binary Search Tree from Preorder Traversal
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 
1 <= preorder.length <= 100
The values of preorder are distinct.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        idx = 0
        def closure(bound = float('inf')):
            nonlocal idx
            
            if idx == len(preorder):
                return None
            
            val = preorder[idx]
            
            if val > bound:
                return None
            
            idx += 1
            node = TreeNode(val)
            node.left = closure(val)
            node.right = closure(bound)
            return node
        
        return closure()
