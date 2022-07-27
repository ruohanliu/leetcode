# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
            #tree #binarysearch #important

            O(logn * logn)
        """
        def check(k,d):
            node = root
            lo = 0
            hi = 2**d-1
            for _ in range(d):
                mid = (lo+hi) // 2
                if k>mid:
                    node = node.right
                    lo = mid+1
                else:
                    node = node.left
                    hi = mid
            return node

        if not root:
            return 0
        depth = -1
        node = root
        while node:
            depth += 1
            node = node.left
        # lo = 0 in case of single root tree
        lo = 0
        hi = 2**(depth)-1
        while lo < hi:
            mid = (lo+hi)//2 + 1
            print(lo,mid,hi,depth,check(mid,depth))
            if check(mid,depth):
                lo = mid
            else:
                hi = mid-1
        return 2**(depth) + lo


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