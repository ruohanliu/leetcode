from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        """
            #monostack
            mono decreasing stack
        """
        monoStack = []
        n = len(height)
        ans = 0
        for i in range(n):
            while monoStack and height[monoStack[-1]] < height[i]:
                currBarIndex = monoStack.pop()
                if monoStack:
                    ans += (min(height[i],height[monoStack[-1]]) - height[currBarIndex]) * (i-monoStack[-1]-1)
            monoStack.append(i)
        return ans

    def trap_dp(self, height: List[int]) -> int:
        """
            #dp
        """
        n = len(height)
        # dp[i] stores the prev max height
        dp_left = [0] * n
        dp_right = [0] * n
        dp_left[0] = height[0]
        dp_right[n-1] = height[n-1]
        for i in range(1, n):
            dp_left[i] = max(dp_left[i-1], height[i])
        for i in range(n-2, -1, -1):
            dp_right[i] = max(dp_right[i+1], height[i])

        ans = 0
        for i in range(n):
            ans += max(0, min(dp_left[i], dp_right[i]) - height[i])
        return ans

    def trap_pointer(self, height: List[int]) -> int:
        """
            #dp
        """
        n = len(height)
        ans = 0
        l = 0
        r = n-1
        lh = height[l]
        rh = height[r]
        while l < r:
            if lh > rh:
                r -= 1
                ans += max(0, min(lh, rh)-height[r])
                rh = max(rh, height[r])
            else:
                l += 1
                ans += max(0, min(lh, rh)-height[l])
                lh = max(lh, height[l])
        return ans