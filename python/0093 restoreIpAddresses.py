from turtle import back
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
            #dfs #backtrack #ipaddress
        """
        def isValidBlock(block):
            try:
                value = int(block)
                if value <= 255 and value >= 0 and str(value) == block:
                    return True
            except:
                return False

        # backtrack stores the start index and length of each ip address block
        backtrack = []
        ans = []
        l = 0
        n = 1

        while True:
            minRemain = 4-len(backtrack)
            maxRemain = (4-len(backtrack))*3

            if l == len(s) and minRemain == 0:
                ans.append(".".join(s[l:l+n] for l, n in backtrack))
                l,n = backtrack.pop()
                n += 1
            elif n > 3 or len(s)-l < minRemain or len(s)-l > maxRemain:
                if not backtrack:
                    break
                l,n = backtrack.pop()
                n += 1
            else:
                if isValidBlock(s[l:l+n]):
                    backtrack.append((l,n))
                    l = l+n
                    n = 0
                else:
                    n += 1
        return ans
s = Solution()
print(s.restoreIpAddresses("25525511135"))
