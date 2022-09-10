class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        """
            #google
        """
        c = Counter(changed)
        ans = []
        if len(changed) % 2 == 1:
            return []
        for x in sorted(c,key = abs):
            if c[x] > c[2*x]:
                return []
            if x == 0:
                ans += [x] * (c[x]//2)
                c[x] -= c[x]
            else:
                ans += [x] * c[x]
                c[2*x] -= c[x]
        if len(ans) == len(changed) // 2:
            return ans
        else:
            return []
