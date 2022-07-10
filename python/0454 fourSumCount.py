class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
            #ksum #important

            related:1995 Count Special Quadruplets
        """
        cnt = 0
        m = collections.defaultdict(int)
        for a in A:
            for b in B:
                m[a + b] += 1
                
        for c in C:
            for d in D:
                cnt += m[-(c + d)]
                
        return cnt

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = collections.defaultdict(int)
        lists = [A, B, C, D]

        def nSumCount() -> int:
            addToHash(0, 0)
            return countComplements(len(lists) // 2, 0)

        def addToHash(i: int, total: int) -> None:
            if i == len(lists) // 2:
                m[total] = m[total] + 1
            else:
                for a in lists[i]:
                    addToHash(i + 1, total + a)

        def countComplements(i: int, complement: int) -> int:
            if i == len(lists):
                return m[complement]
            cnt = 0
            for a in lists[i]:
                cnt += countComplements(i + 1, complement - a)
            return cnt

        return nSumCount()