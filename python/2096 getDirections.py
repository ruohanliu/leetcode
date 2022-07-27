# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import copy


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
            #tree #dfs
        """
        def lca(root):
            if not root:
                return None
            if root.val == startValue or root.val == destValue:
                return root
            left = lca(root.left)
            right = lca(root.right)

            if left and right:
                return root
            return left or right

        lcaNode = lca(root)
        destSteps = []
        startSteps = []
        def dfs(root,step):
            nonlocal startSteps,destSteps
            if root:
                if root.val == startValue:
                    startSteps = step.copy()
                elif root.val == destValue:
                    destSteps = step.copy()

                step.append("L")
                dfs(root.left,step)
                step[-1] = "R"
                dfs(root.right,step)
                step.pop()
        dfs(lcaNode,[])
        return "".join(["U"] * len(startSteps) + destSteps)

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        destSteps = []
        startSteps = []
        def dfs(root,step):
            nonlocal startSteps,destSteps
            if root:
                if root.val == startValue:
                    startSteps = step.copy()
                elif root.val == destValue:
                    destSteps = step.copy()

                step.append("L")
                dfs(root.left,step)
                step[-1] = "R"
                dfs(root.right,step)
                step.pop()
        dfs(root,[])
        
        i = 0
        while i < len(startSteps) and i <len(destSteps) and startSteps[i] == destSteps[i]:
            i+=1
        return "".join(["U"] * (len(startSteps)-i) + destSteps[i:])