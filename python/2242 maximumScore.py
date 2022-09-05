class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        """
            #graph
        """
        adjList = defaultdict(list)
        for a,b in edges:
            if len(adjList[a]) < 3:
                heapq.heappush(adjList[a],(scores[b],b))
            else:
                heapq.heappushpop(adjList[a],(scores[b],b))
            if len(adjList[b]) < 3:
                heapq.heappush(adjList[b],(scores[a],a))
            else:
                heapq.heappushpop(adjList[b],(scores[a],a))
        return max([sum(scores[i] for i in [a,b,aa,bb]) for a,b in edges for _,aa in adjList[a] for _,bb in adjList[b] if a != bb != aa != b],default = -1)