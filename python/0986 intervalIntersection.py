from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
            #interval #merge

            choose while loop condition carefully, avoid using while True.
        """
        ans = []
        p1 = 0
        p2 = 0
        n1 = len(firstList)
        n2 = len(secondList)
        if not n1 or not n2:
            return ans
        while p1 < n1 and p2 < n2:
            lo = max(firstList[p1][0],secondList[p2][0])
            hi = min(firstList[p1][1],secondList[p2][1])
            if lo <= hi:
                ans.append([lo,hi])
            if firstList[p1][1] >= secondList[p2][1]:
                p2 += 1
            else:
                p1 += 1
        return ans

    def intervalIntersection_2(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        prefix_sum = 0
        overlap_start = 0
        for time,status in sorted((x for interval in firstList+secondList for x in ((interval[0],1),(interval[1],-1))),key = lambda y: (y[0],-y[1])):
            prefix_sum += status
            if prefix_sum == 2:
                overlap_start = time
            elif prefix_sum == 1 and status == -1:
                ans.append([overlap_start,time])
        return ans



s = Solution()
print(s.intervalIntersection_2([[4,7],[8,14]],[[3,4]]))