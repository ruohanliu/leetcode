class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
            #binarysearch
        """
        def check(nums,size):
            ans = 0
            for n in nums:
                q,m = divmod(n,size)
                ans += q+ (1 if m else 0) - 1
            return ans
        lo = 1
        hi = 10**9
        while lo <hi:
            mid = (lo+hi) // 2

            if check(nums,mid) > maxOperations:
                lo = mid+1
            else:
                hi = mid
        return lo 