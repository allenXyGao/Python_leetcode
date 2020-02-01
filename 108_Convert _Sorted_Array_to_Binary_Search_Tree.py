# Leetcode 108: Convert Sorted Array to Binary Search Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    Basically, the height-balanced restriction means that at each step 
    one has to pick up the number at the middle as a root 

    '''

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        return self.dfs(nums, 0, len(nums) - 1)
    
    def dfs(self, nums, start, end):
        # exit: start > end
        if start > end:
            return
        # exit: if start == end, we can choose any of them
        if start == end:
            return TreeNode(nums[start])
        
        # find the middle
        mid = (start + end) // 2
        # choose the middle as a root
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, start, mid - 1)
        root.right = self.dfs(nums, mid + 1, end)
        
        return root




'''

手动运行一遍例子：[-10, -3, 0, 5, 9], we assume the left middle as a root
first, start = 0, end = 4, mid = (0 + 4) // 2 = 2 -- > we set the root to be TreeNode(0)
        0
then execute the code: root.left = dfs(nums, start, mid - 1) i.e. focus on [-10, -3] and now start = 0, end = mid - 1 = 1
the new mid = (0 + 1) // 2 = 0 -> we set the root to be TreeNode(-10)  
       0
 -10
continuously, we execute the code: root.left = dfs(nums, start, mid - 1), i.e. focus on [-3], start = 0, end = mid- 1 = -1
start > end --> return None, so the left child of TreeNode(-10) is None
          0
     -10
  None
then back to the root -10 and execute the code root.right = dfs(nums, mid + 1, end), i.e. new start = 1, end = 1
start == end, return TreeNode(3), back to the root -10, then back to the root 0
         0
     -10
  None  -3
Finally we have the tree, and back to the root 0
           0
     -10        5   
  None  -3   None  9
       

'''
