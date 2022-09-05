class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
            #unionfind
        """
        def find(v):
            _v = v
            while v != uf[v]:
                v = uf[v]
            while _v != v:
                uf[_v],_v = v,uf[_v]
            return v
        def union(u,v):
            u = find(u)
            v = find(v)
            if u == v:
                return False
            if size[u] > size[v]:
                size[u]+=size[v]
                uf[v] = u
            else:
                size[v] += size[u]
                uf[u] = v
            return True
        
        uf = list(range(n))
        size = [1] * n
        uf[firstPerson] = 0
        size[0] += 1

        for _,grp in itertools.groupby(sorted(meetings,key = lambda x: x[2]),key = lambda x: x[2]):
            seen = set()
            for u,v,_ in grp:
                seen.add(u)
                seen.add(v)
                union(u,v)
                
            for v in seen:
                if find(v) != 0:
                    uf[v] = v
        return [i for i in range(n) if find(i) == 0]


    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
            #naive
        """
        time = set()
        adjList = defaultdict(set)
        for a,b,t in meetings:
            adjList[t,a].add(b)
            adjList[t,b].add(a)
            time.add(t)
            
        secrets = set([0,firstPerson])
        for t in sorted(time):
            new = set([x for p in secrets for x in adjList[t,p] if x not in secrets])
            while new:
                secrets |= new
                new = set([x for p in new for x in adjList[t,p] if x not in secrets])
        
        return secrets

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
            #groupby #bfs
            mlogm + m
        """
        secrets = set([0,firstPerson])
        for _,grp in itertools.groupby(sorted(meetings,key = lambda x: x[2]),key = lambda x: x[2]):
            adjList = defaultdict(list)
            queue = deque()
            for a,b,_ in grp:
                adjList[a].append(b)
                adjList[b].append(a)
            queue = deque(secrets&set(adjList.keys()))
            while queue:
                for _ in range(len(queue)):
                    a = queue.popleft()
                    for aa in adjList[a]:
                        if aa not in secrets:
                            secrets.add(aa)
                            queue.append(aa)
        return secrets