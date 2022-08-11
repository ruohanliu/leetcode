class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
            #dp #lis #binarysearch
            related 300
        """
        n = len(nums)
        inc = [1] * n
        dec = [1] * n
        temp = [nums[0]]
        for i in range(1,n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                j = bisect.bisect_left(temp,nums[i])
                temp[j] = nums[i]
            inc[i] = len(temp)

        temp = [nums[-1]]
        for i in reversed(range(n-1)):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                j = bisect.bisect_left(temp,nums[i])
                temp[j] = nums[i]
            dec[i] = len(temp)
        
        ans = n
        for i in range(1,n-1):
            if inc[i] > 1 and dec[i] > 1:
                ans = min(ans,n-inc[i]-dec[i]+1)
        return ans