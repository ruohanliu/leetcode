from itertools import accumulate
from typing import List
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        """
            #prefixsum #important
            itertools.accumulate

            iterate on left side (first cut i), find min j that meet the criteria, and min k that DOES NOT meet the criteria. [j:k) is the range of valid 2nd cut
                sum(mid) >= sum(left): ps[j] >= 2 * ps[i]
                sum(right) >= sum(mid): ps[-1] - ps[k] >= ps[k] - ps[i]
            the above relations only depend on i. it could be that j == k
        """
        n = len(nums)
        ans = 0
        prefixSum = list(accumulate(nums))
        mod = 10**9 + 7

        j = 0
        k = 0
        for i in range(n-2):
            if prefixSum[i] * 3 > prefixSum[-1]:
                break
            j = max(i+1,j)
            while j < n-1 and prefixSum[j] < 2 * prefixSum[i]:
                j += 1
            k = max(j,k)
            while k < n-1 and 2 * prefixSum[k] <= prefixSum[-1] + prefixSum[i]:
                k += 1
            ans = (ans + k-j) % mod

        return ans