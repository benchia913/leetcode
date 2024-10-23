#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # the two nodes are leaves
        # strategy is to use a recursion

        # four stats to track at every node
        # height of left subtree
        # height of right subtree
        # max diameter of left subtree
        # max diameter of right subtree

        # recursion function
        def count_distance(node):
            # Base cases first
            if node == None:
                return 0, 0 # height of tree and max diameter
            elif node.left == None and node.right == None:
                return 1, 0
            else:
                lheight, lmaxdiameter = count_distance(node.left)
                rheight, rmaxdiameter = count_distance(node.right)
                height = max(lheight, rheight) + 1 # increment height at each level
                maxdiameter = max(lheight + rheight, lmaxdiameter, rmaxdiameter)
                return height, maxdiameter
            
        height, maxdiameter = count_distance(root)

        return maxdiameter
            

        
        
# @lc code=end

