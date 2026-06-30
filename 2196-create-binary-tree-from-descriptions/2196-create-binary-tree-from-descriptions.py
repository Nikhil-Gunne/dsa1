# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        childs = set()
        for pars,_,_ in descriptions:
            childs.add(pars)
        for par,child,isLeftChild in descriptions:
            if par not in nodes:
                nodes[par] = TreeNode(par)
            parent = nodes[par]
            nodes[child] = TreeNode(child) if child not in nodes else nodes[child]
            childs.discard(child)
            if isLeftChild:
                parent.left = nodes[child]
            else:
                parent.right = nodes[child]
            
        
        return nodes[list(childs)[0]]
        
                

            


    

