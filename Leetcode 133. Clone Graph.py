# Leetcode 133. Clone Graph
'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    
    def __init__(self):
        # visited is a hash map with 
        # key: node in the original graph
        # val: node copied
        self.visited = {}
    
 
    def cloneGraph(self, node):
        # 分两步： 先clone node 再clone 邻居！！
        """
        :type node: Node
        :rtype: Node
        """
        # step 0: exit of the recursive
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        
        # step 1: to clone the nodes
        # the neighbors of clone_node is set to be [], which waited to be connected
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        
        # step 2: to clone the neighbors (since the graph is a connected)
        if node.neighbors:
            for ne in node.neighbors:
                clone_node.neighbors.append(self.cloneGraph(ne))
        
        # output
        return clone_node