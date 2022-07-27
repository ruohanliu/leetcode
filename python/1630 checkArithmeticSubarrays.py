from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
            #segmenttree #furtherstudy
        """
        m = len(l)
        ans = []
        for i in range(m):
            _max = float("-inf")
            _min = float("inf")
            for j in range(l[i], r[i]+1):
                _max = max(_max, nums[j])
                _min = min(_min, nums[j])
            step = (_max - _min) / (r[i] - l[i]+1)
            curr = True
            if step != int(step):
                curr = False
            else:
                step = int(step)
                temp = 0
                for j in range(l[i], r[i]+1):
                    rank =  (nums[j] - _min) / step
                    if rank != int(rank):
                        break
                    rank = int(rank)
                    temp +=  1 << rank
                curr = (1 << (step+1)) - 1 == temp
            ans.append(curr)
        return ans
