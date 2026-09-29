# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ret = []


        def dfs(ret: List[int], node: Optional[TreeNode]):
            if node is None:
                return
            dfs(ret,node.left)
            ret.append(node.val)
            dfs(ret,node.right)
        dfs(ret,root)
        return ret