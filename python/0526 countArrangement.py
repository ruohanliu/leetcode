class Solution:
    def countArrangement(self, n: int) -> int:
        def helper(i,nums):
            if i == 1:
                return 1
            return sum(helper(i-1,nums - {x}) for x in nums if i % x == 0 or x % i == 0)

        return helper(n,set(range(1,n+1)))