class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
            #lca

            related
        """
        p1 = p
        q1 = q
        while p1 != q1:
            p1 = p1.parent if p1.parent else q
            q1 = q1.parent if q1.parent else p
        return p1 or q1