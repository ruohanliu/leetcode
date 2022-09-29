class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
            #stack
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        
        prevMinIndex = [-1] * n
        nextMinIndex = [n] * n
        monoStack = []
        for i in range(n):
            while monoStack and heights[monoStack[-1]] > heights[i]:
                j = monoStack.pop()
                nextMinIndex[j] = i
            monoStack.append(i)
        for i in reversed(range(n)):
            while monoStack and heights[monoStack[-1]] > heights[i]:
                j = monoStack.pop()
                prevMinIndex[j] = i
            monoStack.append(i)
            
        for i in range(n):
            r = nextMinIndex[i]
            l = prevMinIndex[i]
            ans = max(ans,heights[i]*(r-l-1))
        return ans