class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        """
            #dp #multistate #important #bitmask
        """
        @cache
        def dp(i,state,intros,extros):
            if intros == extros == 0 or i == N:
                return 0

            # introvert encoded as 01, extrovert 10
            # only consider the neighbor above and to the left
            up = 3 & state
            left = (3<<shift & state) >> shift

            _state = state >> 2
            ans = dp(i+1,_state,intros,extros)

            if intros:
                score = 120 + score_map[up,1] + (score_map[left,1] if i % n else 0)
                ans = max(ans,score + dp(i+1,_state + (1 << shift),intros-1,extros))
            
            if extros:
                score = 40 + score_map[up,2] + (score_map[left,2] if i % n else 0)
                ans = max(ans,score + dp(i+1,_state + (2 << shift),intros,extros-1))
            return ans

        N = m*n
        if m<n:
            m,n = n,m
        shift = (n-1)*2
        score_map = {(0, 1): 0,        # empty neighbor (0) add introvert (1) to current cell
                    (0, 2): 0,         # empty neighbor (0) add extrovert (2) to current cell
                    (1, 1): -30 - 30,  # introvert neighbor (1) add introvert (1) to current cell
                    (2, 1): 20 - 30,   # extrovert neighbor (2) add introvert (1) to current cell
                    (1, 2): -30 + 20,  # introvert neighbor (1) add extrovert (2) to current cell
                    (2, 2): 20 + 20}   # extrovert neighbor (2) add extrovert (2) to current cell
        return dp(0,0,introvertsCount,extrovertsCount)