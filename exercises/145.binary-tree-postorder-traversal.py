#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # helper recursive function
        def postorder(node):
            # terminating condition first
            # Base Case 1: None node
            if node == None:
                return []
            # Base Case 2: Leaves
            if node.left == None and node.right == None:
                return [node.val]
            # Recursive case
            else:
                return postorder(node.left) + postorder(node.right) + [node.val]
            
        return postorder(root)

        
# @lc code=end

