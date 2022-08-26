class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
            #slidingwindow 

            O(n) space
        """
        c=defaultdict(int)
        c[0] += 1
        ans = 0
        ps = 0
        for i,x in enumerate(nums):
            ps += x
            ans += c[ps-goal]
            c[ps] += 1
        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
            O(1) space
        """
        def atMost(k):
            if k < 0:
                return 0
            i = 0
            ans = 0
            for j,x in enumerate(nums):
                k -= x
                while k<0:
                    k+=nums[i]
                    i+=1
                ans += j-i+1
            return ans
        return atMost(goal) - atMost(goal-1)