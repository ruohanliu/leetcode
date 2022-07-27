class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
            #monostack #prefixsum #important 

            If x1 < x2 and P[x2] <= P[x1], then opt(y) can never be x1, as if P[x1] <= P[y] - K, then P[x2] <= P[x1] <= P[y] - K but y - x2 is smaller. This implies that our candidates x for opt(y) will have increasing values of P[x].

            If opt(y1) = x, then we do not need to consider this x again. For if we find some y2 > y1 with opt(y2) = x, then it represents an answer of y2 - x which is worse (larger) than y1 - x.

            Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
        """
        n = len(nums)
        ps = 0
        # deck stores [index,prefixSum]
        monoDeque = deque([[0,0]])
        ans = n+1
        for i,num in enumerate(nums):
            ps += num
            while monoDeque and monoDeque[-1][1] >= ps:
                monoDeque.pop()
            while monoDeque and monoDeque[0][1] <= ps - k:
                ans = min(ans, i+1 - monoDeque.popleft()[0])

            monoDeque.append([i+1,ps])
                
        return ans if ans < n+1 else -1
