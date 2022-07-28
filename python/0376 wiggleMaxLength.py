class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
            #dp
            related 1567
        """
        n = len(nums)
        if n < 2:
            return n
        up = [0]*n
        dn = [0]*n
        up[0] = 1
        dn[0] = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                up[i] = dn[i-1]+1
                dn[i] = dn[i-1]
            elif nums[i] < nums[i-1]:
                up[i] = up[i-1]
                dn[i] = up[i-1]+1
            else:
                up[i] = up[i-1]
                dn[i] = dn[i-1]
        return max(up[-1],dn[-1])

    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        up = 1
        dn = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                up = dn+1
            elif nums[i] < nums[i-1]:
                dn = up+1
        return max(up,dn)