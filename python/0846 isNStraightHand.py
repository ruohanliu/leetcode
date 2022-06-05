from typing import List
class Solution:
    def isNStraightHand_slow(self, hand: List[int], groupSize: int) -> bool:
        """
            take away
                dict keys/values/items are not subscriptable, convert to list first
                min()/max() does not support empty iterable

            #collections #Counter
        """
        from collections import Counter
        hand_len = len(hand)
        if hand_len % groupSize > 0:
            return False
        
        hand.sort()
        hand_counter = Counter(hand)
        while len(hand_counter) > 0:
            group_cards = list(hand_counter.keys())[:groupSize]
            if len(group_cards) < groupSize:
                return False
            for i in range(len(group_cards)-1):
                if group_cards[i] != group_cards[i+1] - 1:
                    return False
            groups = min(hand_counter[card] for card in group_cards)
            hand_counter -= {card:groups for card in group_cards}
        return True

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
            #collections #deque #whileloop #trim #careful
        """
        from collections import deque
        hand_len = len(hand)
        if hand_len % groupSize > 0:
            return False
        
        hand.sort()
        q = deque([],groupSize)
        i = 0
        cnt = 0 
        while i < hand_len:
            cnt += 1
            if i == hand_len - 1 or hand[i+1] != hand[i]:
                q.append([hand[i],cnt])
                if len(q) == groupSize:
                    size = q[0][1]
                    for j in range(0,groupSize):
                        q[j][1] -= size
                        if q[j][1] < 0:
                            return False
                    while q and q[0][1] == 0:
                        q.popleft()
                else:
                    if i == hand_len - 1:
                        return False
                if i < hand_len - 1 and q and hand[i+1] != hand[i] + 1:
                    return False
                cnt = 0
            i += 1
        return not q

s = Solution()
print(s.isNStraightHand([4,3,3,4,1,2,2,4],4))