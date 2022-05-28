from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
            see 0560
            hash set store cumulative sum mod k

            Consideration:
                if sum % k == 0 then there is a solution
                or the same mod appears the 2nd time then there is a solution
        """
        mod = 0
        dict = {0:-1}
        for i in range(0,len(nums)):
            mod  = (mod + nums[i]) % k
            if mod in dict:
                if i - dict[mod] > 1:
                    return True
            else:
                dict[mod] = i
        return False
s = Solution()
print(s.checkSubarraySum([0],7))
