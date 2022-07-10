class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        """
            #binarysearch
        """
        n1 = sorted(nums1)
        m = len(nums1)
        
        currSaved = 0
        ans = 0
        for x1,x2 in zip(nums1,nums2):
            diff = abs(x1-x2)
            ans += diff
            if currSaved < diff:
                i = bisect.bisect_left(n1,x2)
                potential = min(x2 - n1[i-1] if i > 0 else inf, n1[i] - x2 if i < m else inf)
                currSaved = max(currSaved,diff - potential)
        return (ans - currSaved) % (10**9+7)
