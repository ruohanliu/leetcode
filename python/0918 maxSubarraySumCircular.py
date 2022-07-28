class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
            #kadane #algorithm #important
        """
        n = len(nums)
        ans = float("-inf")
        curr = 0
        for num in nums:
            curr = max(curr + num,num)
            ans = max(ans,curr)
        maxRightSum = [0] * n
        rightSum = 0
        for i in reversed(range(n)):
            rightSum += nums[i]
            maxRightSum[i] = rightSum if i == n-1 else max(rightSum,maxRightSum[i+1])
        
        leftSum = 0
        for i in range(n-1):
            leftSum += nums[i]
            rightSum = maxRightSum[i+1]
            ans = max(ans,leftSum + rightSum)
        return ans

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            # Maximum non-empty subarray sum
            ans = float("-inf")
            curr = 0
            for x in nums:
                curr = max(curr+x, x)
                ans = max(ans, curr)
            return ans
        
        n = len(nums)
        total = sum(nums)
        if n == 1:
            return total
        
        ans1 = kadane(nums)
        # total - min subarray sum
        # if the min Subarray sum we choose is the entire array, the resulting two interval subarray [0, i] + [j, N-1] would be empty
        # Therefore doing min kadane twice
        ans2 = total + kadane(-nums[i] for i in range(1, n))
        ans3 = total + kadane(-nums[i] for i in range(n - 1))
        return max(ans1, ans2, ans3)