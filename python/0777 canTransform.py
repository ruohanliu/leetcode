class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
            #clever
            
            LXXLXRLXXL
            XLLXRXLXLX
        """
        if start.replace("X","") != end.replace("X",""):
            return False
        
        n = len(start)
        i = 0
        j = 0
        while i<n and j<n:
            while i<n and start[i] == "X":
                i += 1
            while j<n and end[j] == "X":
                j += 1
            
            if i == n == j:
                return True
            if i == n or j == n or start[i] != end[j]:
                return False
            if (start[i] == "L" and i<j) or (start[i] == "R" and i>j):
                return False
            # neight at the end, start[i] == end[j]
            i+=1
            j+=1
        return True