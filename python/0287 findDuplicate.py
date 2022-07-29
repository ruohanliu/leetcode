from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
            #rotation #unionfind #important
        """
        while nums[0] != nums[nums[0]]:
            nums[nums[0]],nums[0] = nums[0],nums[nums[0]]
        return nums[0]

    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]

        # Restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate

    def findDuplicate(self, nums: List[int]) -> int:
        """
            #linkedlist #cycle #important

            choose 0 because it is guaranteed to link to another
        """
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        other = 0
        while other != slow:
            other = nums[other]
            slow = nums[slow]
        return slow

    def findDuplicate(self, nums: List[int]) -> int:
        """
            #binarysearch        
        """
        lo = 1
        hi = len(nums)
        while lo<hi:
            mid = (lo+hi) //2
            cnt = sum(x<=mid for x in nums)
            if cnt <= mid:
                lo = mid+1
            else:
                hi = mid
        return lo
                