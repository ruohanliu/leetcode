class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
            #tree #BST #linkedlist
        """
        def rec(root):
            left = root
            right = root
            if root.left:
                first,last = rec(root.left)
                last.right = root
                root.left = last
                left = first

            if root.right:
                first,last = rec(root.right)
                first.left = root
                root.right = first
                right = last
                
            return (left,right)
        
        if not root:
            return None
        first,last = rec(root)
        first.left = last
        last.right = first
        return first
