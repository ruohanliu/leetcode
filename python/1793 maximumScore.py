class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        """
            #twopointer #greedy
            score = len*min
        """
        ans = nums[k]
        n = len(nums)
        curr_min = nums[k]
        i = j = k
        for _ in range(n-1):
            if i > 0 and j < n-1:
                if nums[i-1] < nums[j+1]:
                    j+= 1
                else:
                    i -= 1
            elif i > 0:
                i-=1
            else:
                j+=1
                
            curr_min = min(curr_min,nums[j],nums[i])
            ans = max(ans,curr_min * (j-i+1))
        return ans