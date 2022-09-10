# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
            #graph #prune
        """
        a = 0
        # find first person who doesnt know anyone
        for i in range(1,n):
            if knows(a,i):
                a = i
        
        return a if all(knows(i,a) and not knows(a,i) for i in range(n) if i != a) else -1
