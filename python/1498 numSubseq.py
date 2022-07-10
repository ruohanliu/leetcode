class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
            #clever
            subsequence problem can be sorted if we dont use the order

            pow(base,p,mod) is more efficient
        """
        nums.sort()
        n = len(nums)
        ans = 0
        i = 0
        j = n-1
        mod = 10**9+7
        while i<=j:
            if nums[j]+nums[i] > target:
                j-=1
            else:
                ans += pow(2,(j-i),mod)
                i+=1
        return ans % mod