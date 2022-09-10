class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        curr = ps = 0
        for j,(g,c) in enumerate(zip(gas,cost)):
            ps += g-c
            curr += g-c
            if curr < 0:
                i = j+1
                curr = 0
        return i if ps>=0 else -1