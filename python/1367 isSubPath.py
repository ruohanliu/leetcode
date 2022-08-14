# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
            #KMP #furtherstudy
        """
        def dfs(head, root):
            if not head: return True
            if not root: return False
            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        if not head: return True
        if not root: return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def isSubPath(self, head, root):
        A, dp = [head.val], [0]
        i = 0
        node = head.next
        while node:
            while i and node.val != A[i]:
                i = dp[i - 1]
            i += node.val == A[i]
            A.append(node.val)
            dp.append(i)
            node = node.next

        def dfs(root, i):
            if not root: return False
            while i and root.val != A[i]:
                i = dp[i - 1]
            i += root.val == A[i]
            return i == len(dp) or dfs(root.left, i) or dfs(root.right, i)
        return dfs(root, 0)