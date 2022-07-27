from typing import List
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            #dfs #graph

            reversal of all edge direction in DAG does not matter

            Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
        """
        def findOrder(v):
            if perm[v]:
                return False
            
            if temp[v]:
                return True
            
            temp[v] = True
            res = False
            for _v in edges[v]:
                res |= findOrder(_v)
            
            ans.append(v)
            temp[v] = False
            perm[v] = True
            return res

        ans = []
        n = numCourses
        edges = defaultdict(list)
        
        for edge in prerequisites:
            edges[edge[0]].append(edge[1])
        
        perm = [False] * n
        temp = [False] * n 

        for v in range(numCourses):
            if findOrder(v):
                return []
        return ans

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            #topologicalsort #graph #important
        """
        ans = []
        adjList = defaultdict(list)
        inDegree = defaultdict(int)
        
        source = set(range(numCourses))
        for a,b in prerequisites:
            source.discard(a)
            adjList[b].append(a)
            inDegree[a] += 1
        
        while source:
            v = source.pop()
            ans.append(v)
            for _v in adjList[v]:
                inDegree[_v] -= 1
                if inDegree[_v] == 0:
                    source.add(_v)
            del adjList[v]

        return ans if not adjList else []