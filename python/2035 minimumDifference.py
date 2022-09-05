class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
            #math #combination #clever #important
        """
        n = len(nums)//2
        left, right = nums[:n], nums[n:]
        lsum, rsum = sum(left), sum(right)
        
        ans = float("inf")
        for i in range(n+1): 
            # lcombo + rcombo ~ lsum-lcombo + rsum - rcombo
            # 2lcombo - lsum ~ -(2rcombo - rsum)
            vals = sorted(2*sum(combo)-lsum for combo in combinations(left, i))
            for combo in combinations(right, n-i): 
                diff = 2*sum(combo) - rsum
                k = bisect.bisect_left(vals, -diff)
                if k: ans = min(ans, abs(vals[k-1] + diff))
                if k < len(vals): ans = min(ans, abs(vals[k] + diff))
        return ans 