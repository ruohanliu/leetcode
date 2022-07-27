from typing import List
class Solution:
    def sumSubarrayMins_tle(self, arr: List[int]) -> int:
        """
            #dp
            too slow
        """
        n = len(arr)
        ans = 0
        mod = 10**9 + 7
        # dp[i] stores the min of subarray starting at i 
        dp = [0] * n
        for i in range(n):
            dp[i] = arr[i]
            ans = (ans + dp[i]) % mod

        for x in range(1,n):
            for i in range(n-x):
                dp[i] = min(dp[i],arr[x])
                ans = (ans + dp[i]) % mod
        return ans

    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
            #monostack #important
            use monostack to find next min and prev min.
            one side use strictly less and the other side use non-strict less to account for duplicate elements
        """
        n = len(arr)
        ans = 0
        mod = 10**9 + 7

        nextMinIndex = [n] * n
        prevMinIndex = [-1] * n
        monoStack = []
        for i in range(n):
            while monoStack and arr[monoStack[-1]] > arr[i]:
                nextMinIndex[monoStack.pop()] = i
            monoStack.append(i)
        monoStack = []
        for i in range(n-1, -1, -1):
            while monoStack and arr[monoStack[-1]] >= arr[i]:
                prevMinIndex[monoStack.pop()] = i
            monoStack.append(i)

        for i in range(n):
            ans = (ans + arr[i] * (nextMinIndex[i]-i) * (i - prevMinIndex[i])) % mod
        return ans
