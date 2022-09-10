class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
            #digits

            O(nlogn)
        """
        s1 = set([1, 8, 0])
        s2 = set([1, 8, 0, 6, 9, 2, 5])
        def isGood(x):
            s = set([int(i) for i in str(x)])
            return s<=s2 and not (s<=s1)
        return sum(isGood(i) for i in range(n + 1))

    def rotatedDigits(self, n: int) -> int:
        """
            O(logn)
        """
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 8, 2, 5, 6, 9])
        s = set()
        ans = 0
        nums = list(map(int, str(n)))
        # 2815
        for i, v in enumerate(nums):
            for j in range(v):
                if s<=s2 and j in s2:
                    ans += 7**(len(nums) - i - 1)
                if s<=s1 and j in s1:
                    ans -= 3**(len(nums) - i - 1)
            if v not in s2:
                return ans
            s.add(v)
        return ans + (s.issubset(s2) and not s.issubset(s1))