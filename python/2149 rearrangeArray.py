class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
            #shift #furtherstudy
            https://leetcode.com/problems/rearrange-array-elements-by-sign/discuss/1711456/Can-we-do-this-in-place-i.e.-O(1)-space-with-O(n)-time/1233680
        """
        ans = [0] * len(nums)

        pos = 0
        neg = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos += 1
                ans[(pos-1)*2] = nums[i]
            else:
                neg += 1
                ans[(neg-1)*2+1] = nums[i]
        return ans