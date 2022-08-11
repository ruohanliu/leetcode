class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
            #monostack #prefixsum #important 

            If x1 < x2 and P[x2] <= P[x1], then opt(y) can never be x1, as if P[x1] <= P[y] - K, then P[x2] <= P[x1] <= P[y] - K but y - x2 is smaller. This implies that our candidates x for opt(y) will have increasing values of P[x].

            If opt(y1) = x, then we do not need to consider this x again. For if we find some y2 > y1 with opt(y2) = x, then it represents an answer of y2 - x which is worse (larger) than y1 - x.

            Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
        """
        n = len(nums)
        ans = float("inf")
        # use increasing queue to store prefix sum
        # use a sentinel to handle single element input. then it become 1-indexed
        incQueue = deque([(0,0)])
        ps = 0
        for i,x in enumerate(nums):
            ps += x
            while incQueue and incQueue[-1][1] >= ps:
                incQueue.pop()
            while incQueue and ps - incQueue[0][1] >= k:
                ans = min(ans,i+1-incQueue.popleft()[0])
            incQueue.append((i+1,ps))
        return ans if ans < float("inf") else -1