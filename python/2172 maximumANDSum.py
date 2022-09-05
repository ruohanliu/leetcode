class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        """
            #dp #bismask

            base^n - 1 is initial state

            order of placing num does not matter
        """
        @cache
        def dp(i, state):
            if i == len(nums):
                return 0
            ans = 0
            for slot in range(1, numSlots + 1):
                # shift
                bit = 3 ** (slot - 1)
                # capacity remaining for the slot
                if state // bit % 3 > 0:
                    ans = max(ans, (nums[i] & slot) + dp(i + 1, state - bit))
            return ans
        return dp(0, 3 ** numSlots - 1)