from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
            #topologicalsort
        """
        def findOrder(words):
            nonlocal adjList,indegree
            for word in words:
                for c in word:
                    indegree[c] += 0
            for prev,curr in zip(words,words[1:]):
                if len(prev) > len(curr) and prev.startswith(curr):
                    return False
                
                for i in range(min(len(prev),len(curr))):   
                    if prev[i] != curr[i]:
                        if curr[i] not in adjList[prev[i]]:
                            adjList[prev[i]].add(curr[i])
                            indegree[curr[i]] += 1
                        break
            return True

        adjList = defaultdict(set)
        indegree = defaultdict(int)
        if not findOrder(words):
            return ""
        queue = [v for v in indegree if indegree[v] == 0]

        ans = []
        while queue:
            v = queue.pop()
            ans.append(v)
            for _v in adjList[v]:
                indegree[_v] -= 1
                if indegree[_v] == 0:
                    queue.append(_v)
            del adjList[v]
        if adjList:
            return ""
        else:
            return "".join(ans)