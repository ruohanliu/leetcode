from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            #dfs #graph

            There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai
        """
        def isCyclic(v):
            if vChecked[v]:
                return False
            
            if vVisited[v]:
                return True
            
            vVisited[v] = True
            res = False
            for _v in edges[v]:
                res |= isCyclic(_v)
            
            vVisited[v] = False
            vChecked[v] = True
            return res

        n = numCourses
        edges = defaultdict(list)
        
        for edge in prerequisites:
            edges[edge[0]].append(edge[1])
        
        vChecked = [False] * n
        vVisited = [False] * n 

        for v in range(numCourses):
            if isCyclic(v):
                return False
        return True
