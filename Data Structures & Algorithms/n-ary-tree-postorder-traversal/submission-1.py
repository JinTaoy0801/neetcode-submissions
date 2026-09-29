"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        

        ret = []


        def dfs(root: 'Node'):
            if root is None:
                return

            if root.children:
                for i in range( len(root.children)):
                    dfs(root.children[i])

            ret.append(root.val)
        dfs(root)

        return ret
