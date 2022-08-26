from typing import List
class Solution:
    def isNStraightHand_slow(self, hand: List[int], groupSize: int) -> bool:
        """
            take away
                dict keys/values/items are not subscriptable, convert to list first

            #Counter
        """
        c = Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                # reverse to reuse c[i]
                for j in reversed(range(groupSize)):
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
            #deque #important
        """
        c = Counter(hand)
        # group stores the diff of cnt
        group = deque()
        cnt = 0 
        for k in sorted(c):
            if cnt > c[k] or (cnt > 0 and last_k + 1 < k):
                return False
            group.append(c[k] - cnt)
            last_k = k
            cnt = c[k]
            if len(group) == groupSize:
                cnt -= group.popleft()
        return cnt == 0

s = Solution()
print(s.isNStraightHand([4,3,3,4,1,2,2,4],4))