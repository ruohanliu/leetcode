class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s = set(range(1,n+1))
        c = Counter()
        for item in trust:
            s.discard(item[0])
            c[item[1]] += 1
        if len(s) == 1:
            last = s.pop()
            if c[last] == n-1:
                return last
            else: return -1
        else: return -1

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
            celebrity solution
        """

        adjList = defaultdict(set)
        for a,b in trust:
            adjList[a].add(b)
        
        a = 1
        for i in range(2,n+1):
            if i in adjList[a]:
                a = i
        
        return a if all(a in adjList[i] for i in range(1,n+1) if i != a) and not adjList[a] else -1