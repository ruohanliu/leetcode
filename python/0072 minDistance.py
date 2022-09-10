class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        """
            #dp #spaceoptimize #important #distance
        """
        if len(s2) < len(s1):
            s1, s2 = s2, s1

        m = len(s1)
        n = len(s2)

        prev = [0] * (m+1)
        curr = [0] * (m+1)

        for i in range(m):
            prev[i+1] = prev[i] + 1

        # s2
        for i in range(n):
            curr[0] = 1+prev[0]
            # s1
            for j in range(m):
                if s1[j] == s2[i]:
                    curr[j+1] = min(prev[j+1], curr[j], prev[j]-1) + 1
                else:
                    curr[j+1] = min(prev[j+1], curr[j], prev[j]) + 1
            prev, curr = curr, prev
        return prev[-1]
