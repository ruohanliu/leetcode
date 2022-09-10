class Leaderboard:
    """
        #design #leaderboard #sorteddict #microsoft
    """

    def __init__(self):
        from sortedcontainers import SortedDict
        self.scores = SortedDict()
        self.players = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.players:
            self.players[playerId] = score
            if score in self.scores:
                self.scores[score]+=1
            else:
                self.scores[score]=1
        else:
            curr = self.players[playerId]
            self.scores[curr]-=1
            if self.scores[curr] == 0:
                del self.scores[curr]
            
            score = score + curr
            self.players[playerId] = score
            if score in self.scores:
                self.scores[score]+=1
            else:
                self.scores[score] = 1
        

    def top(self, K: int) -> int:
        cnt = 0
        ans = 0
        i = -1
        while cnt < K:
            score,n_players = self.scores.peekitem(i)
            if n_players + cnt < K:
                ans += score * n_players
                cnt += n_players
                i -= 1
            else:
                ans += score * (K-cnt)
                cnt = K
        return ans

    def reset(self, playerId: int) -> None:
        score = self.players[playerId]
        del self.players[playerId]
        self.scores[score]-=1
        if self.scores[score] == 0:
            del self.scores[score]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)