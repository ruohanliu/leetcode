# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
            #tree #important

            or use record parent node and use bfs 
        """
        # return distance between node and target
        def dfs(node):
            if not node:
                return -1
            if node == target:
                addSubtree(node,0)
                return 0
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                # if target is in left subtree
                if left != -1:
                    if left == k-1:
                        ans.append(node.val)
                    addSubtree(node.right,left+2)
                    return left + 1
                # if target is in right subtree
                elif right != -1:
                    if right == k-1:
                        ans.append(node.val)
                    addSubtree(node.left,right+2)
                    return right + 1
                else:
                    return -1

        def addSubtree(node,dist):
            if not node:
                return
            if dist == k:
                ans.append(node.val)
            else:
                addSubtree(node.left,dist+1)
                addSubtree(node.right,dist+1)
                  
        ans = []
        dfs(root)
        return ans