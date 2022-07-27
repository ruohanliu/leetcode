from typing import List
class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        """
            #stack
        """
        n = len(heights)
        leftStack = []
        rightStack = []
        l = k
        r = k
        for _ in range(volume):
            while (l > 0 and heights[l - 1] <= heights[l]):
                l -= 1
                if heights[l] < heights[l+1]:
                    leftStack.append(l)
            while (r < n-1 and heights[r + 1] <= heights[r]):
                r += 1
                if heights[r] < heights[r-1]:
                    rightStack.append(r)
            if leftStack:
                curr = leftStack[-1]
                heights[curr] += 1
                if heights[curr] == heights[curr+1]:
                    leftStack.pop()
                if curr > l:
                    leftStack.append(curr-1)
            elif rightStack:
                curr = rightStack[-1]
                heights[curr] += 1
                if heights[curr] == heights[curr-1]:
                    rightStack.pop()
                if curr < r:
                    rightStack.append(curr+1)
            else:
                heights[k]+=1
                if k > l:
                    leftStack = [k-1]
                if k < r:
                    rightStack = [k+1]
        return heights
