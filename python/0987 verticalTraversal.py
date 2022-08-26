# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            #tree
        """
        mn = float("inf")
        mx = float("-inf")
        verticalOrder = defaultdict(list)
        queue = deque([(root,0,0)])
        while queue:
            node,pos,dep = queue.popleft()
            verticalOrder[pos].append((dep,node.val))
            mn = min(mn,pos)
            mx = max(mx,pos)
            if node.left:
                queue.append((node.left,pos-1,dep+1))
            if node.right:
                queue.append((node.right,pos+1,dep+1))

        return [[x[1] for x in sorted(verticalOrder[pos])] for pos in range(mn,mx+1) if verticalOrder[pos]]
