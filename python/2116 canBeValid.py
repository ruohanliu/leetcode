class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
            #parentheses
            A useful trick (when doing any parentheses validation) is to greedily check balance left-to-right, and then right-to-left.
                Left-to-right check ensures that we do not have orphan ')' parentheses.
                Right-to-left checks for orphan '(' parentheses.
        """
        n = len(s)
        if n % 2 == 1: return False
        wild = op = cl = 0
        for i in range(n):
            if locked[i] == "0": wild += 1
            elif s[i] == "(": op += 1
            elif s[i] == ")": cl += 1
            if wild + op < cl:
                return False
        wild = op = cl = 0
        for i in reversed(range(n)):
            if locked[i] == "0": wild += 1
            elif s[i] == ")": op += 1
            elif s[i] == "(": cl += 1
            if wild + op < cl:
                return False
        return True
