class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """
            #bfs

            Bezout's Identity states that for some integers x, y, z,a, b, x*a+y*b = z*gcd(a,b)
        """
        visited = set([(x,True) for x in forbidden] + [(x,False) for x in forbidden]+[(0,True)])
        queue = [(0,True)]
        cnt = 0
        furthest = max(x,max(forbidden)) + a + b
        while queue:
            print(queue)
            nextSteps = []
            cnt += 1
            while queue:
                p,back = queue.pop()
                if p == x:
                    return cnt - 1
                n = p+a
                if n <= furthest and (n,back) not in visited :
                    nextSteps.append((n,True))
                    visited.add((n,True))
                    visited.add((n,False))
                
                if a!=b and back:
                    n = p-b
                    if n > 0 and (n,back) not in visited:
                        nextSteps.append((n,False))
                        visited.add((n,False))
            queue = nextSteps
        return -1