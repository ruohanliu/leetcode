class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
            #slidingwindow #important
            related 1358
        """
        def atMost(k):
            i = 0
            ans = 0
            odd = 0
            for j,x in enumerate(nums):
                odd += x % 2
                while odd > k:
                    odd -= nums[i] % 2
                    i += 1
                ans += j-i+1
            return ans
        
        return atMost(k) - atMost(k-1)

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        ans = 0
        cnt = 0
        for j,x in enumerate(nums):
            # initialize left side # of qualifying subarrays to 0 when right side meets with a qualifying element
            # count left side size when condition is met
            # accumulate left side size for every right element
            if x % 2:
                k -= 1
                cnt = 0
            while k == 0:
                k += nums[i] % 2
                i += 1
                cnt += 1
            ans += cnt
        return ans