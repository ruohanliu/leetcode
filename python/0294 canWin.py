class Solution:
    def canWin(self, currentState: str) -> bool:
        """
            #game #gametheory #furtherstudy
            #Sprague-Grundy
            https://leetcode.com/problems/flip-game-ii/discuss/73954/Theory-matters-from-Backtracking(128ms)-to-DP-(0ms)
        """
        def game(s):
            if s.find("++") == -1:
                return False
            for i in range(n-1):
                if s[i:i+2] == "++":
                    if not (game(s[:i]) or game(s[i+2:])):
                        return True
            return False
        n = len(currentState)
        return game(currentState)

    def canWin(self, currentState: str) -> bool:
        g, G = [0], 0
        for p in map(len, re.split('-+', currentState)):
            while len(g) <= p:
                g += min(set(range(p)) - {a^b for a, b in zip(g, g[-2::-1])}),
            G ^= g[p]
        return G > 0