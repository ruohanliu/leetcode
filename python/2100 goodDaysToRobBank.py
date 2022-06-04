from typing import List
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return [i for i in range(len(security))]

        before = [0] * len(security)
        after = [0] * len(security)
        
        cnt = 0
        
        for i in range(1,len(security)):
            if security[i] <= security[i-1]:
                cnt += 1
            else:
                cnt = 0
            before[i] = cnt
        cnt = 0
        for i in range(len(security)-2,-1,-1):
            if security[i] <= security[i+1]:
                cnt += 1
            else:
                cnt = 0
            after[i] = cnt

        ans = []
        for i in range(len(security)):
            if before[i] >= time and after[i] >= time:
                ans.append(i)
            
        return ans

s = Solution()
print(s.goodDaysToRobBank([5,3,3,3,5,6,2],2))