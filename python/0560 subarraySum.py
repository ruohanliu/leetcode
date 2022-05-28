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

            cannot use sliding window because of negative values
        """
        ans = 0
        s = 0
        d = {0:1}
        for i in range(len(nums)):
            s += nums[i]
            if (s-k) in d:
                ans += d[s-k]
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        return ans
s = Solution()
print(s.subarraySum([1,2,3,0,-1,-2,1,3],2))

        