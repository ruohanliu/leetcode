class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
            #stack
        """
        stack = []
        for c in num:
            while k and stack and stack[-1]>c:
                stack.pop()
                k-=1
            stack.append(c)
        if k:
            stack = stack[:len(stack)-k]
            
        if not stack:
            return "0"
        return str(int("".join(stack)))
