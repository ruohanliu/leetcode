class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
            #slidingwindow #important

            related 904 395 340
            count of subarray with k distinct element
        """
        def subarrayWithAtMostK(nums,k):
            count = defaultdict(int)
            ans = 0
            i = 0
            for j,f in enumerate(nums):
                count[f] += 1
                while len(count) > k:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0:
                        del count[nums[i]]
                    i += 1
                ans += j-i+1
            return ans

        return subarrayWithAtMostK(nums,k)-subarrayWithAtMostK(nums,k-1)