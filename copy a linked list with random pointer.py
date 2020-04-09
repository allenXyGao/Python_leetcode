class Solution(object):
    
    def __init__(self):
        # creating a visited dictionary yo hold old node reference as "key"
        # and new node reference as the "value"
        self.visited = {}
    
    def getCloneNode(self, node):
        # if node exists:
        if node:
            # case 1: if its in the visited dictionary
            if node in self.visited:
                # then return the new node reference from the dicionary
                return self.visited[node]
            # case 2: if not
            else:
                # create a new node, save the reference in the dict and return it
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        # if node does not exist, the return None
        return None
                
        
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        old_node = head
        # creating the new head node
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node
        
        # iterate on the linked list until all nodes are cloned
        while old_node != None:
            # get the clones of the nodes referenced by random and next pointer
            new_node.random = self.getCloneNode(old_node.random)
            new_node.next = self.getCloneNode(old_node.next)
            
            # move one step ahead in the linked list
            old_node = old_node.next
            new_node = new_node.next
        
        return self.visited[head]
    
    ## O(N) time make one pass over the original linked list
    ## O(N) space dictionary containing mapping from old list nodes to new list nodes and there are N nodes.