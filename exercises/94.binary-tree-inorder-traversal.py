#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # helper function
        def inorder(node):
            # two terminating conditions as base case
            # Base Case 1: to handle cases when None is passed into function instead 
            # of a TreeNode object
            if node == None:
                return []
            # Base Case 2: to handle leaves
            elif node.left == None and node.right == None:
                return [node.val]
            # Recursive case
            else:
                return inorder(node.left) + [node.val] + inorder(node.right)
            

        return inorder(root)


        
# @lc code=end

