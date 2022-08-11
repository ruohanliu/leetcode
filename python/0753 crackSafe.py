class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """
            #google #de-Bruijn #dfs #greedy
        """
        ans = str(k-1) * (n-1)
        visited = set()
        for _ in range(k**n):
            last = ans[-n+1:] if n > 1 else ""
            for d in range(k):
                candidate = last+str(d)
                if candidate not in visited:
                    visited.add(candidate)
                    ans += str(d)
                    break
        return ans


    def crackSafe(self, n: int, k: int) -> str:
        def dfs():
            nonlocal ans,visited
            if len(ans) == target:
                return True
            last = ans[-n+1:] if n > 1 else ""
            for d in reversed(range(k)):
                candidate = last + str(d)
                if candidate not in visited:
                    curr = len(ans)
                    ans += str(d)
                    visited.add(candidate)
                    if dfs():
                        return True
                    visited.remove(candidate)
                    ans = ans[:curr]
            return False

        ans = "0" * (n-1)
        visited = set()
        target = k**n+n-1
        dfs()
        return ans