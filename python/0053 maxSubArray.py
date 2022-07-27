class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = curr
        for n in nums[1:]:
            curr = max(curr+n,n)
            ans = max(ans,curr)
            
        return ans

    def maxSubArray(self, nums: List[int]) -> int:
        """
            #dividenconquer
        """
        def dnc(l,r):
            if l>r:
                return float("-inf")
            mid = (l+r)//2
            lSum = 0
            rSum = 0
            curr = 0
            for i in range(mid-1,l-1,-1):
                curr += nums[i]
                lSum = max(lSum,curr)
            curr = 0
            for i in range(mid+1,r+1):
                curr += nums[i]
                rSum = max(rSum,curr)
            return max(lSum + nums[mid] + rSum,dnc(l,mid-1),dnc(mid+1,r))
        return dnc(0,len(nums)-1)