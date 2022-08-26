class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
            #bucketsort
        """
        mn,mx,n = min(nums),max(nums),len(nums)
        if n == 1:
            return 0
        # ceil. ans will be at least gap
        gap = (mx-mn-1) // (n-1) + 1
        # n-1 buckets, each bucket stores min + i*gap
        buckets = [[] for _ in range(n-1)]
        for x in nums:
            idx = n - 2 if x == mx else (x-mn)//gap
            buckets[idx] += x,
        mn_mx = [(min(bucket),max(bucket)) for bucket in buckets if bucket]

        return max([b[0] - a[1] for a,b in zip(mn_mx,mn_mx[1:])],default = mn_mx[0][1] - mn_mx[0][0])
