from sys import prefix
from typing import List
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        """
            #dp #prefixsum #important

            O(N*2) is trivial, O(N) is the way to go.
            Let f(i) denotes number of valid subarrays ends at i, f(i) = f(i-1) + g(i)
            Here g(i) is the number of times the following appearred, where j<=i-1
                if num is 1:
                    prefixSum[i-1] - prefixSum[j] == 0
                if num is 0:
                    prefixSum[i-1] - prefixSum[j] == 1

            For prefixsum problem:
                sum(i:j] can be computed  as prefixSum(j) - prefixSum(i)
                initialize memo/counter
        """
        from collections import Counter
        # prefix_sum denotes the number of net 1's
        prefixsum = 0
        # count[prefix_sum] denotes the number of times prefix_sum occurs
        count = Counter({0: 1})
        # dp denotes the # of valid subarrays that end at current position
        dp = 0

        ans = 0
        mod = 10**9+7
        for n in nums:
            # find out # of subarrays end at i-1 and sum == 0
            # for such subarrays: prefixSum[i-1] - prefixSum[j] == 0 or prefixSum[i-1] == prefixSum[j]
            # translate to: find out # of times prefixSum[i-1] appearred
            if n:
                # i-1
                dp += count[prefixsum]
                prefixsum += 1
            # find out # of subarrays end at i-1 and sum == 1
            # for such subarrays: prefixSum[i-1] - prefixSum[j] == 1
            # translate to: find out # of times prefix[i] appearred
            else:
                # i
                prefixsum -= 1
                dp -= count[prefixsum]
            ans = (ans + dp) % mod
            count[prefixsum] += 1

        return ans

s = Solution()
print(s.subarraysWithMoreZerosThanOnes([1,1,0,1,0,1]))