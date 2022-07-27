class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        """
            #math
        """
        ans = []
        queue = [(n,2,[])]
        while queue:
            target,curr,factors = queue.pop()
            while curr * curr <= target:
                if target % curr == 0:
                    queue.append((target//curr,curr,factors+[curr]))
                    ans.append(factors+[target//curr,curr])
                curr += 1
        return ans