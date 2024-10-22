#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # prepare helper recursive function
        def count_levels(node):
            # terminating conditions
            if node == None:
                return 0
            # start accumulating count from leaves
            elif node.left == None and node.right == None:
                return 1
            else:
                return min([x for x in [count_levels(node.left), 
                                        count_levels(node.right)] if x > 0]) + 1
            
        return count_levels(root)
        
# @lc code=end

