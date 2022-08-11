class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
            #dp #bitmask
            O(n*2^n)
        """
        @cache
        def dp(state):
            i = state.bit_count()
            if i == n:
                return 0
            return min((nums1[i]^nums2[j]) + dp(state | 1 << j) for j in range(n) if state & 1 << j == 0)

        n = len(nums1)
        return dp(0)