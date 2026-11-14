"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None:None}
        copy = head
         
        while copy: # making the old_to_new dictionary a map the old nodes to a new node value only node
            old_to_new[copy] = Node(copy.val)
            copy = copy.next

        copy = head
        while copy: # now adding the pointers to the new nodes as each node can point to eachother 
            old_to_new[copy].next = old_to_new[copy.next]
            old_to_new[copy].random = old_to_new[copy.random]
            copy = copy.next

        return old_to_new[head]
        
    

        
        
            
        