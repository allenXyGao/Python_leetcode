# Leetcode 129. Sum Root to Leaf Numbers

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.total = 0
        self.dfs(root, 0)
        return self.total
    
    def dfs(self, root, cur_sum):
        # exit
        if not root:
            return
        if not root.left and not root.right:
            self.total += cur_sum * 10 + root.val
            return
        
        self.dfs(root.left, cur_sum * 10 + root.val)
        self.dfs(root.right, cur_sum * 10 + root.val)