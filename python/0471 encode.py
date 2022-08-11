class Solution:
    def encode(self, s: str) -> str:
        """
            #dp #string
        """
        @cache
        def dp(s):
            n = len(s)
            if n < 5:
                return s
            i = (s+s).find(s,1)
            one = f"{n//i}[{dp(s[:i])}]" if i < n else s
            multi = [dp(s[:i])+dp(s[i:]) for i in range(1,n)]
            return min([s,one]+multi,key = len)
        return dp(s)