class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        """
            #twopointer #important #bit #furtherstudy
            
            no need to honor i<j constraint for diff[i] + diff[j] > 0

            https://leetcode.com/problems/count-pairs-in-two-arrays/discuss/1249860/BIT-vs.-Binary-Search
        """
        # diff[i] > -diff[j]
        diff = sorted(x1-x2 for x1,x2 in zip(nums1,nums2))
        n = len(diff)
        ans = 0
        i = 0
        j = n-1
        while i<j:
            if diff[i] > -diff[j]:
                ans += j-i
                j-=1
            else:
                i += 1
        return ans