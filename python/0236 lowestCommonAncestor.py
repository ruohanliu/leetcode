# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            #tree #lca #binarylifting
            related 1740 2277
        """
        def dfs(root):
            if root:
                if root == p or root == q:
                    return root
                
                left = dfs(root.left)
                right = dfs(root.right)

                if left and right:
                    return root
                return left or right

        return dfs(root)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,parents,depth):
            nonlocal dp,depths,tree
            if node:
                tree[node.val] = node
                depths[node.val] = depth
                for bit in range(m):
                    if 1<<bit <= len(parents):
                        dp[node.val][bit] = parents[-(1<<bit)]
                parents.append(node.val)
                if node.left:
                    dfs(node.left,parents,depth+1)
                if node.right:
                    dfs(node.right,parents,depth+1)
                parents.pop()
        def kAncestor(val,k):
            while k:
                bit = k.bit_length() - 1
                val = dp[val][bit]
                k -= 1<<bit
            return val

        def lca(a,b):
            if depths[a] > depths[b]:
                return lca(b,a)
            b = kAncestor(b,depths[b] - depths[a])
            lo = 0
            hi = depths[a]
            while lo < hi:
                mid = (lo+hi) // 2
                if kAncestor(a,mid) == kAncestor(b,mid):
                    hi = mid
                else:
                    lo = mid + 1
            return kAncestor(a,lo)

        n = 10**5
        m = n.bit_length()
        tree = {}
        dp = defaultdict(lambda: [0]*m)
        depths = defaultdict(int)            
        dfs(root,[],0)
        return tree[lca(p.val,q.val)]
