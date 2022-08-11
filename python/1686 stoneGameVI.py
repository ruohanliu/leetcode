class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        """
            #greedy
        """
        n = len(aliceValues)
        diffValues = sorted([(x+y,i) for i,(x,y) in enumerate(zip(aliceValues,bobValues))])
        alice = sum(aliceValues[diffValues[i][1]] for i in range(n-1,-1,-2))
        bob = sum(bobValues[diffValues[i][1]] for i in range(n-2,-1,-2))
        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0