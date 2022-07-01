class Solution:
    def sortColors_countingsort(self, nums: List[int]) -> None:
        """
            #sort #important #algorithm #countingsort

            sort 3 color in place
        """
        c = Counter(nums)
        i = 0
        for k in range(3):
            nums[i:i+c[k]] = [k] * c[k]
            i+=c[k]
        return nums

    def sortColors_onepass(self, nums: List[int]) -> None:
        l = 0
        r = len(nums)-1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i],nums[l] = nums[l],nums[i]
                l+=1
                i+=1
            elif nums[i] == 2:
                nums[i],nums[r] = nums[r],nums[i]
                r-=1
            else:
                i += 1