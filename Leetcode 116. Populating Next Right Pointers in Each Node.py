# Leetcode 116. Populating Next Right Pointers in Each Node
'''
you are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
 If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

'''
Level-order traversal
Essentially, at each step, we record the size of the queue and that always corresponds
to all the nodes on a particular level. Once we have this size, we only process these many elements
and no more. By the time we are done processing size number of elements, the queue would contain 
exactly all the nodes on the next level.

while (!Q.empty())
{   
    size = Q.size()
    for i in range(size)
    {
       node = Q.pop()
       Q.push(node.left)
       Q.push(node.right)
    }

}
'''



class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        
        from collections import deque
        que = deque([root])
        while que:
            size = len(que)
            for i in range(size):
                ele = que.popleft()
                
                if i < size - 1:
                    ele.next = que[0]
                if ele.left:
                    que.append(ele.left)
                if ele.right:
                    que.append(ele.right)
        return root
        