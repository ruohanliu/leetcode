class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
            #BST #preorder
        """
        stack = []
        low = float('-inf')
        for p in preorder:
            if p < low:
                return False
            while stack and stack[-1] < p:
                low = stack.pop()
            stack.append(p)
        return True