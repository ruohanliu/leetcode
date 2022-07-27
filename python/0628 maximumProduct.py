class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
            #heap
        """
        largest_3 = heapq.nlargest(3,nums)
        smallest_2 = heapq.nsmallest(2,nums)
        return max(largest_3[0]*largest_3[1]*largest_3[2],max(largest_3)*smallest_2[0]*smallest_2[1])