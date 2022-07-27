from itertools import accumulate

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
            #heap

            #prefixsum #binarysearch #furtherstudy
            https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/733047/Python-Binary-Search-Time-O(NlogSum(A))
        """
        n = len(nums)
        heap = [(x,i) for i,x in enumerate(nums)]
        heapq.heapify(heap)

        ans = 0
        for i in range(right):
            num,idx = heapq.heappop(heap)
            if i+1>=left:
                ans += num
            if idx<n-1:
                heapq.heappush(heap,(num+nums[idx+1],idx+1))
        return ans % (10**9+7)

    def rangeSum_naive(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
            O(n^2)
            #prefixsum #important
            there are n*(n+1)/2 non-empty subarray
        """
        prefixSum = [0]+list(accumulate(nums))
        n = len(nums)
        return sum(sorted([prefixSum[i]-prefixSum[j] for i in range(1,n+1) for j in range(i)])[left-1:right]) % (10**9+7)