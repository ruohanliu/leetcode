from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
            naive method: two loops, cumulative sum, O(n^2)

            best method: hashmap, store cumulative sum as key,
                one pass, O(n) and O(n)
                current sum - previous sum  = 1 current index solution
                s - (s-k) = k
                #dp #difficult #clever 

            related:
                0560

            cannot use sliding window because of negative values
        """
        cumulative_sum = 0
        min_index_dict = {0:-1}
        ans = 0
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            if cumulative_sum - k in min_index_dict:
                ans = max(ans,i - min_index_dict[cumulative_sum - k])
            if cumulative_sum not in min_index_dict:
                min_index_dict[s] = i
        return ans
s = Solution()
print(s.subarraySum([1,-1,5,-2,3],3))
