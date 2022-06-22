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

        for i in reversed(range(m)):
            prev[i] = prev[i+1] + 1

        for i in reversed(range(n)):
            curr[m] = 1+prev[m]
            for j in reversed(range(m)):
                if s1[j] == s2[i]:
                    curr[j] = min(prev[j], curr[j+1], prev[j+1]-1) + 1
                else:
                    curr[j] = min(prev[j], curr[j+1], prev[j+1]) + 1
            prev, curr = curr, prev
        return prev[0]
