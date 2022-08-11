class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
            #hard #important #sortedset #kadane

            related
                560 Subarray Sum Equals K
                862 Shortest Subarray with Sum at Least K
                85  maximalRectangle
                53  maxSubArray
            
            O(m^2nlogn)
        """
        from sortedcontainers import SortedSet
        ans = float("-inf")
        if len(matrix) < len(matrix[0]):
            m = len(matrix)
            n = len(matrix[0])
            for i in range(m):
                rowSum = [0]*n
                for r in range(i,m):
                    for c in range(n):
                        rowSum[c] += matrix[r][c]

                    # kadane
                    curr = 0
                    currMax = float("-inf")
                    for num in rowSum:
                        curr = max(curr+num,num)
                        currMax = max(currMax,curr)

                    if currMax <= k:
                        ans = max(ans,currMax)
                        if ans == k:
                            return ans
                    # nlogn
                    else:
                        ps = 0
                        ss = SortedSet([0])
                        for num in rowSum:
                            ps += num
                            idx = ss.bisect_left(ps-k)
                            if idx < len(ss):
                                ans = max(ans,ps - ss[idx])
                                if ans == k:
                                    return ans
                            ss.add(ps)
        else:
            m = len(matrix)
            n = len(matrix[0])
            for i in range(n):
                colSum = [0]*m
                for c in range(i,n):
                    for r in range(m):
                        colSum[r] += matrix[r][c]

                    # kadane
                    curr = 0
                    currMax = float("-inf")
                    for num in colSum:
                        curr = max(curr+num,num)
                        currMax = max(currMax,curr)

                    if currMax <= k:
                        ans = max(ans,currMax)
                        if ans == k:
                            return ans
                    # nlogn
                    else:
                        ps = 0
                        ss = SortedSet([0])
                        for num in colSum:
                            ps += num
                            idx = ss.bisect_left(ps-k)
                            if idx < len(ss):
                                ans = max(ans,ps - ss[idx])
                                if ans == k:
                                    return ans
                            ss.add(ps)
        return ans