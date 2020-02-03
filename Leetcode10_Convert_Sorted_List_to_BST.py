# Leetocde 109. Convert Sorted List to Binary Search Tree
'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        return self.dfs(head)
    
    def dfs(self, head):
        if not head:
            return
        # get the middle
        mid = self.get_middle(head)
        # set the middle to be the root
        root = TreeNode(mid.val)
        
        if mid == head: # case when there is just one element in the linked list
            return root
        
        root.left = self.dfs(head)
        root.right = self.dfs(mid.next)
        
        return root
       
    
    
    def get_middle(self, head):
        '''
        get_middle gets the middle element of the linked list and seperates the whole linked list
        into three pieces: (1). head to prev; (2). mid; (3). mid.next to end
        '''
        prev = None # to disconnect the left half from the middle node
        slow = head
        fast = head
        
        # iterate to find the middle
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # handling the case when slow = head, e.g. 10 -> None
        if prev:
            prev.next = None
        
        # return mid
        return slow