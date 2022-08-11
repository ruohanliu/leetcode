class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
            #dp #important

            dp can use defaultdict
        """
        # dp[val] = # of operation
        dp = {-1:0}
        arr2.sort()
        m = len(arr2)
        for curr in arr1:
            tmp = defaultdict(lambda: float("inf"))
            # iterate over every possible val in prev position
            for last in dp:
                # if do not replace
                if curr > last:
                    tmp[curr] = min(tmp[curr],dp[last])
                # replace
                j = bisect.bisect_right(arr2,last)
                if j < m:
                    tmp[arr2[j]] = min(tmp[arr2[j]],dp[last] + 1)
            dp = tmp
        return min(dp.values()) if dp else -1