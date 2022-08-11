class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        """
            #bitwise
            related 201

            O( n * log( max( arr[i] ) ) )
        """
        ans = float("inf")
        # prefix and
        pa = set()
        for x in arr:
            pa = {x&y for y in pa}|{x}
            ans = min(ans,min(abs(y  - target) for y in pa))
        return ans

    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = float("inf")
        maxInt = 2**31 - 1
        pa = set()
        for x in arr:
            tmp = set()
            pa.add(maxInt)
            for y in pa:
                y &= x
                ans = min(ans,abs(y - target))
                if y > target:
                    tmp.add(y)
            pa = tmp
        return ans
