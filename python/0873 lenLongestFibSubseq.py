class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
            #dp
        """        
        n = len(arr)
        dp = defaultdict(lambda:2)
        idx = {}
        for i in range(n):
            c = arr[i]
            for j in range(i-1,0,-1):
                b = arr[j]
                a = c-b
                if a >= b:
                    break
                if a in idx:
                    dp[j,i] = dp[idx[a],j] + 1
                
            idx[arr[i]] = i
        mx = max(dp.values(),default=0)
        return mx if mx>=3 else 0