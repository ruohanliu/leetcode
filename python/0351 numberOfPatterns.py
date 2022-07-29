class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """
            #backtrack

            1379 are symmetric and 2468 are symmetric
        """
        def backtrack(n,progress):
            nonlocal ans
            if n == 0:
                ans += 1 if progress[0] == 5 else 4
                return
            
            curr = progress[-1] if progress else 0
            if curr == 0:
                unvisited = set([1,2,5])
            else:
                unvisited = set(range(1,10)) - set(progress)
            if curr == 1:
                if 2 not in progress: unvisited.discard(3)
                if 5 not in progress: unvisited.discard(9)
                if 4 not in progress: unvisited.discard(7)
            elif curr == 3:
                if 2 not in progress: unvisited.discard(1)
                if 5 not in progress: unvisited.discard(7)
                if 6 not in progress: unvisited.discard(9)
            elif curr == 7:
                if 4 not in progress: unvisited.discard(1)
                if 5 not in progress: unvisited.discard(3)
                if 8 not in progress: unvisited.discard(9)
            elif curr == 9:
                if 6 not in progress: unvisited.discard(3)
                if 5 not in progress: unvisited.discard(1)
                if 8 not in progress: unvisited.discard(7)
            elif curr == 2:
                if 5 not in progress: unvisited.discard(8)
            elif curr == 4:
                if 5 not in progress: unvisited.discard(6)
            elif curr == 6:
                if 5 not in progress: unvisited.discard(4)
            elif curr == 8:
                if 5 not in progress: unvisited.discard(2)

            for i in unvisited:
                progress.append(i)
                backtrack(n-1,progress)
                progress.pop()
        ans = 0
        for i in range(m,n+1):
            backtrack(i,[])
        return ans