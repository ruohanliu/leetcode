from typing import List
from collections import defaultdict
import heapq
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        """
            #topologicalsort

            Given a string s, reconstruct the lexicographically smallest permutation perm and return it.
        """
        adjList = defaultdict(set)
        inDegree = defaultdict(int)
        for i,c in enumerate(s):
            if c == "I":
                adjList[i].add(i+1)
                inDegree[i+1] += 1
            else:
                adjList[i+1].add(i)
                inDegree[i] += 1
        n = len(s) + 1
        heap = [v for v in range(n) if inDegree[v] == 0]
        heapq.heapify(heap)
        ans = [0] * n
        cnt = 0 
        while heap:
            cnt += 1
            v = heapq.heappop(heap)
            ans[v] = cnt
            for _v in adjList[v]:
                inDegree[_v] -= 1
                if inDegree[_v] == 0:
                    heapq.heappush(heap,_v)
        return ans

    def findPermutation(self, s: str) -> List[int]:
        """
            #stack #important
        """
        stack = []
        ans = []
        n = len(s) + 1
        for i,c in enumerate(s):
            if c == "I":
                stack.append(i+1)
                while stack:
                    ans.append(stack.pop())
            else:
                stack.append(i+1)
        stack.append(n)
        while stack:
            ans.append(stack.pop())
        return ans

    def findPermutation(self, s: str) -> List[int]:
        """
            in-place reverse
        """
        n = len(s) + 1
        ans = [i for i in range(1,n+1)]
        j = 0
        for i,c in enumerate(s):
            if c == "I":
                if i+1 > j:
                    ans[j:i+1] = ans[j:i+1][::-1]
                j = i+1
            else:
                continue
        ans[j:] = ans[j:][::-1]
            
        return ans