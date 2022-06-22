class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
            #binarysearch 

            the key to binary search is discovering monotonicity.
            designing condition function

            check(mid) may not return the exact number
        """
        def check(x):
            cnt = 0
            for r in range(1,m+1):
                add = min(n,x//r)
                if add == 0:
                    return cnt
                cnt += add
            return cnt

        lo,hi=1,m*n
        while lo<hi:
            mid = (lo+hi) // 2
            if check(mid) < k:
                lo = mid+1
            else:
                hi = mid
        return lo

s = Solution()
print(s.findKthNumber(45,12,471))