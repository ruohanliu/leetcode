from typing import List
class Solution:
    def mctFromLeafValues_dp(self, arr: List[int]) -> int:
        """
            #dp 
            O(N^3)
        """
        # dp[i][j] denotes min sum result
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        def divideConquer(i,j):
            nonlocal dp,arr
            if dp[i][j] >= 0:
                print(i,j,dp[i][j])
                return dp[i][j]
            if j-i == 1:
                dp[i][j] = arr[i] * arr[j]
                print(i,j,dp[i][j])
                return dp[i][j]
            
            
            ans = float("inf")
            for k in range(i,j):
                ans = min(ans,divideConquer(i,k) + divideConquer(k+1,j) + max(arr[i:k+1]) * max(arr[k+1:j+1]))
            dp[i][j] = ans
            print(i,j,dp[i][j])
            return dp[i][j]

        return divideConquer(0,n-1)

    def mctFromLeafValues_nlogn(self, arr: List[int]) -> int:
        """
            #sortedlist #important
            O(nlogn)

            Always group the 2 smallest leaf nodes, and discard the smallest leaf node
        """
        from sortedcontainers import SortedList
        n = len(arr)
        sortedArr = sorted((x,i) for i, x in enumerate(arr))
        origArr = SortedList((i,x) for i, x in enumerate(arr))
        ans = 0

        for i in range(n):
            val,j = sortedArr[i] 
            k = origArr.index((j,val))
            if k == 0:
                ans += origArr[k+1][1] * val
            elif k == len(origArr) - 1:
                ans += origArr[k-1][1] * val
            else:
                ans += min(origArr[k-1][1],origArr[k+1][1]) * val
            origArr.pop(k)
        return ans

    def mctFromLeafValues_stack(self, arr: List[int]) -> int:
        """
            #monostack #important
            O(n)

            Group at any local minimum, and discard the local minimum
        """
        n = len(arr)
        ans = 0
        monoStack = []

        for i in range(n):
            while monoStack and monoStack[-1] < arr[i]:
                ans += monoStack.pop() * min(monoStack[-1] if monoStack else float("inf"), arr[i])
            monoStack.append(arr[i])

        while len(monoStack) > 1:
            ans += monoStack.pop() * monoStack[-1]
        return ans
