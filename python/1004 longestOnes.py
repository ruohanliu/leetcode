class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
            #slidingwindow
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -=1
                
            if k<0:
                if nums[left] == 0:
                    k+=1
                left+=1
        return right - left + 1
            
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        ans = float("-inf")
        for j,x in enumerate(nums):
            if x == 0:
                k-=1
            while k < 0:
                if nums[i] == 0:
                    k += 1
                i+=1
            ans = max(ans,j-i+1)
        return ans