class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        """
            #lis #lcs
            transform lcs problem O(mn) into lis problem O(mlogn)
            nums1 elements are distinct
        """
        idxMap = {x:i for i,x in enumerate(nums1)}
        nums = [idxMap[x] for x in nums2 if x in idxMap]
        if not nums:
            return len(nums1)
        lis = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                lis[bisect.bisect_left(lis,nums[i])] = nums[i]
        return len(nums1) - len(lis)