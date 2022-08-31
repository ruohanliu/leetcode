class Solution:
    def largestVariance(self, s: str) -> int:
        """
            #kadane #hard
        """
        c = Counter(s)
        ans = 0
        for a,b in itertools.permutations(c,2):
            if max(c[a],c[b]) - 1 <= ans:
                continue
            ps = 0
            prev_ps = 0
            prev_min_ps = float("inf")
            for x in s:
                if x not in (a,b):
                    continue
                if x == a:
                    ps += 1
                else:
                    ps -= 1
                    # previous array to subtract must end with b
                    prev_min_ps = min(prev_min_ps,prev_ps)
                    prev_ps = ps
                ans = max(ans,ps-prev_min_ps)
        return ans