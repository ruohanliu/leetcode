class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
            #dp #relation #backtrack #greedy
        """
        tuplify = lambda balance,fn: tuple(sorted((p,b) for p,b in balance.items() if fn(p)))
        @cache
        def dp(balance):
            if not balance:
                return 0
            ans = float("inf")
            balance = {p:b for p,b in balance}
            for size in range(2,len(balance)+1):
                for group in combinations(balance.keys(),size):
                    if sum(balance[p] for p in group) == 0:
                        ans = min(ans,size-1 + dp(tuplify(balance,lambda x:x not in group)))
            return ans
        
        balance = defaultdict(int)
        c = defaultdict(list)
        for f,t,amt in transactions:
            balance[f] -= amt
            balance[t] += amt
        temp = [(p,b) for p,b in balance.items()]
        ans = 0
        for p,b in temp:
            if b == 0:
                del balance[p]
            elif c[-b]:
                del balance[p]
                del balance[c[-b].pop()]
                ans += 1
            else:
                c[b].append(p)
        return ans + dp(tuplify(balance,lambda x:True))

    def minTransfers(self, transactions: List[List[int]]) -> int:
        def backtrack(balance):
            if not balance:
                return 0
            for size in range(1,len(balance)+1):
                ans = float("inf")
                for group in combinations(balance.keys(),size):
                    if sum(balance[p] for p in group) == 0:
                        temp = {}
                        for p in group:
                            temp[p] = balance[p]
                            del balance[p]
                        ans = min(ans,size-1 + backtrack(balance))
                        balance |= temp
            return ans
        
        balance = defaultdict(int)
        for f,t,amt in transactions:
            balance[f] -= amt
            balance[t] += amt
        return backtrack(balance)