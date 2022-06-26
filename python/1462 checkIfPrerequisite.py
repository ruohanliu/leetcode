from collections import defaultdict
from msilib.schema import Component
from typing import DefaultDict, List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
            #topologicalsort
            unionfind does not work for directed graph
        """
        adjList = defaultdict(list)
        inDegree = defaultdict(int)
        prerequisiteMap = defaultdict(set)

        for a,b in prerequisites:
            adjList[a] += b,
            inDegree[b] += 1
        
        freeCourses = [v for v in range(numCourses) if inDegree[v] == 0]
        while freeCourses:
            course = freeCourses.pop()
            for nextCourse in adjList[course]:
                prerequisiteMap[nextCourse].add(course)
                prerequisiteMap[nextCourse] |= prerequisiteMap[course]
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    freeCourses.append(nextCourse)
            del adjList[course]


        return [a in prerequisiteMap[b] for a,b in queries]