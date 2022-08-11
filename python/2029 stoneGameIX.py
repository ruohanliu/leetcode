class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        """
            #backtrack

            pop/append must not be interrupted by shortcut return
        """
        # returns True if Alice wins
        def backtrack(i,c,m):
            if i == n:
                return False
            for j in range(3):
                if c[j] and (j+m) % 3:
                    c[j] -= 1
                    res = backtrack(i+1,c,(j+m)%3)
                    c[j] += 1
                    if (i % 2 == 1) ^ res:
                        return i % 2 == 0
            # if Alice's turn, return False
            # if Bob's   turn, return True
            return i % 2 == 1
        
        c = Counter([x % 3 for x in stones])
        # even 0s cancel out. optimize
        c[0] = c[0] % 2
        n = c.total()
        return backtrack(0,c,0)