#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # helper recursive function
        def preorder(node):
            # terminating condition first
            # Base Case 1: None node
            if node == None:
                return []
            # Base Case 2: Leaves
            if node.left == None and node.right == None:
                return [node.val]
            # Recursive case
            else:
                return [node.val] + preorder(node.left) + preorder(node.right)
            
        return preorder(root)

        
# @lc code=end

