from typing import List
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        """
            #dp #important #relation

            O(N*2) is trivial, O(N) is the way to go.
            Let f(i) denotes number of valid subarrays ends at i, f(i) = f(i-1) + g(i)
            Here g(i) is the number of times the following appearred, where j<=i-1
                if num is 1:
                    ps[i-1] - ps[j] == 0
                if num is 0:
                    ps[i-1] - ps[j] == 1

            For prefixsum problem:
                sum(i:j] can be computed  as ps(j) - ps(i)
                initialize memo/counter
        """
        from collections import Counter
        # prefix_sum denotes the number of net 1's
        ps = 0
        # count[prefix_sum] denotes the number of times prefix_sum occurs
        count = Counter({0: 1})
        # dp denotes the # of valid subarrays that end at current position
        dp = 0

        ans = 0
        mod = 10**9+7
        for x in nums:
            # find out # of subarrays end at i-1 and sum == 0
            # translate to: find out # of times ps[i-1] appearred
            if x:
                dp += count[ps]
                ps += 1
            # find out # of subarrays end at i-1 and sum == 1
            # translate to: find out # of times prefix[i] appearred
            else:
                dp -= count[ps-1]
                ps -= 1
            ans = (ans + dp) % mod
            count[ps] += 1

        return ans