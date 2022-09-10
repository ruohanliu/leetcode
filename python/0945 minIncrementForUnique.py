class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
            #greedy #unionfind #important #databricks

            O(nlogn)
        """
        ans = need = 0
        for x in sorted(nums):
            ans += max(need - x, 0)
            need = max(need,x) + 1
        return ans

    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
            O(n+klogk)
        """
        c = Counter(nums)
        ans = 0
        need = 0
        for x in sorted(c):
            ans += max(need-x,0) * c[x] + (c[x]-1) * c[x] // 2
            need = max(need,x) + c[x]
        return ans

    def minIncrementForUnique(self, nums):
        """
            amortized O(n)
        """
        uf = {}
        def find(x):
            if x in uf:
                uf[x] = find(uf[x]+1)
            else:
                uf[x] = x
            return uf[x]
        return sum(find(a) - a for a in nums)