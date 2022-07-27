import collections
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
            #bfs

            bfs use queue (FIFO), dfs use stack (LIFO)
        """
        if s[-1] != "0":
            return False
        n = len(s)
        r = 1
        bfs = collections.deque([0])
        while bfs:
            i = bfs.popleft()
            for j in range(max(i+minJump, r), min(n, i+maxJump+1)):
                if s[j] == "0":
                    if j == n-1:
                        return True
                    bfs.append(j)
            r = i+maxJump+1
        return False

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
            #dp #important

            sliding window: when moving to next element, there is one more candidate to jump from: i-minJump. There is one fewer candidate to jump from: i - maxJump - 1
            bool can be added to int
        """
        # dp[i] denotes whether s[i] is reachable
        # pre denotes the number of previous location that we can jump from
        dp = [c == '0' for c in s]
        pre = 0
        for i in range(1, len(s)):
            if i >= minJump:
                pre += dp[i - minJump]
            if i > maxJump:
                pre -= dp[i - maxJump - 1]
            dp[i] &= pre > 0
        return dp[-1]
