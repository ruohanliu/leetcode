class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
            #monostack #prefixsum #important 

            If x1 < x2 and P[x2] <= P[x1], then opt(y) can never be x1, as if P[x1] <= P[y] - K, then P[x2] <= P[x1] <= P[y] - K but y - x2 is smaller. This implies that our candidates x for opt(y) will have increasing values of P[x].

            If opt(y1) = x, then we do not need to consider this x again. For if we find some y2 > y1 with opt(y2) = x, then it represents an answer of y2 - x which is worse (larger) than y1 - x.

            Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
        """
        # store prefix sum in mono queue
        n = len(nums)
        # incQueue[0] is the min ps and therefore ps[-1] - incQueue[0] is maximized
        # use a sentinel to handle single element input. then it become 1-indexed
        incQueue = deque([(0,-1)])
        ps = 0
        ans = float("inf")
        for i,x in enumerate(nums):
            ps += x
            while incQueue and incQueue[-1][0] > ps:
                incQueue.pop()
            incQueue.append((ps,i))
            while ps - incQueue[0][0] >=k:
                _,j = incQueue.popleft()
                ans = min(ans,i-j)
        return ans if ans < float("inf") else -1
            