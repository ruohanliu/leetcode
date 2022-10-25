class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
            #monostack
            related 2282
        """
        n = len(heights)
        ans = [0] * n
        stack = []
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] < v:
                ans[stack.pop()] += 1
            # only the immediate left higher can see curr
            if stack:
                ans[stack[-1]] += 1
                if heights[stack[-1]] == v:
                    stack[-1] = i
                    continue
            stack.append(i)
        return ans