# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        
        def avg(node):
            if node is None:
                return [0,0,0]
            
            leftSum,leftNodes,leftCnt = avg(node.left)
            rightSum,rightNodes,rightCnt = avg(node.right)

            
                
            return [leftSum+rightSum+node.val,leftNodes+rightNodes+1,leftCnt+rightCnt + (1 if (leftSum + rightSum + node.val) // (leftNodes + rightNodes + 1) == node.val else 0)]
        
        
        return avg(root)[2]


        