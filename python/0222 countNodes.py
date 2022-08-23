# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
            #tree #binarysearch #important #hard

            O(logn * logn)

            level: 1~2^(level-1)
            binary search on the # of nodes in the deepest level
        """
        def check(k,n):
            curr = root
            while n > 1:
                n //= 2
                if k <= n:
                    curr = curr.left
                else:
                    curr = curr.right
                    k -= n
            return True if curr else False
            
        if not root:
            return 0
        level = 0
        curr = root
        while curr:
            level += 1
            curr = curr.left
        
        complete = 2**(level-1)
        lo = 1
        hi = 2**(level-1)
        while lo<hi:
            mid = (lo+hi)//2 + 1
            if check(mid,complete):
                lo = mid
            else:
                hi = mid-1
                
        return 2**(level-1)-1+lo


    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
            O(n)
        """
        def dfs(node,i):
            if node:
                l = dfs(node.left,2*i)
                r = dfs(node.right,2*i+1)
            else:
                return 0
            return max(l,r,i)
                
        return dfs(root,1)