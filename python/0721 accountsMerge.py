class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
            #unionfind #graph
        """
        def find(a):
            _a = a
            while a != uf[a]:
                a = uf[a]
            while _a != a:
                _a,uf[_a] = uf[_a],a
            return a 

        def union(a,b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            if size[a] > size[b]:
                size[a] += size[b]
                uf[b] = a
            else:
                size[b] += size[a]
                uf[a] = b
            return True

        n = len(accounts)
        uf = list(range(n))
        size = [0] * n
        # every email to their id
        idx = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in idx:
                    union(i, idx[email])
                idx[email] = find(i)

        # every combined id to its emails
        ans = defaultdict(list)
        for email, i in idx.items():
            ans[find(i)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
        
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAccount = defaultdict(list)
        adjList = defaultdict(list)
        for i,account in enumerate(accounts):
            adjList[i].append(i)
            for email in account[1:]:
                emailToAccount[email].append(i)
        
        for email in emailToAccount:
            for i,j in itertools.combinations(emailToAccount[email],2):
                adjList[i].append(j)
                adjList[j].append(i)
        
        ans = []
        while adjList:
            i,queue = adjList.popitem()
            name = accounts[i][0]
            ids = set([i])
            while queue:
                j = queue.pop()
                if j in adjList:
                    ids.add(j)
                    queue.extend(adjList[j])
                    del adjList[j]
            emails = set()
            for i in ids:
                emails |= set(accounts[i][1:])
            ans.append([name] + sorted(emails))
        return ans
            
                
        