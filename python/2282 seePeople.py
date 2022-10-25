class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        """
            #monostack
            related 1944
        """
        m = len(heights)
        n = len(heights[0])
        ans = [[0]*n for _ in range(m)]
        
        for i in range(m):
            stack = []
            for j in range(n):
                while stack and heights[i][stack[-1]] < heights[i][j]:
                    ans[i][stack.pop()] += 1
                if stack:
                    ans[i][stack[-1]] += 1
                    if heights[i][stack[-1]] == heights[i][j]:
                        stack[-1] = j
                        continue
                stack.append(j)
                    
        for j in range(n):
            stack = []
            for i in range(m):
                while stack and heights[stack[-1]][j] < heights[i][j]:
                    ans[stack.pop()][j] += 1
                if stack:
                    ans[stack[-1]][j] += 1
                    if heights[stack[-1]][j] == heights[i][j]:
                        stack[-1] = i
                        continue
                stack.append(i)
        return ans
                    
            