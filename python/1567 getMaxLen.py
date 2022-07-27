from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """
            #math #important #dp

            O(1) dp
        """
        pos=neg=ans=0
        for n in nums:
            if n == 0:
                neg = pos = 0
            elif n > 0:
                pos += 1
                neg += 1 if neg > 0 else 0
            else:
                temp = pos
                pos = neg + 1 if neg > 0 else 0
                neg = temp + 1
            ans = max(ans,pos)
        return ans
