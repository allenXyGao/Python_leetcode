# Leetcode 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        self.max_sum = - sys.maxsize
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, root):
        # exit
        if not root:
            return
        
        left_max = max(0, self.dfs(root.left))
        right_max = max(0, self.dfs(root.right))
        self.max_sum = max(self.max_sum, root.val + left_max + right_max)
        
        return root.val + max(left_max, right_max)