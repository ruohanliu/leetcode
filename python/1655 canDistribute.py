class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        """
            #dp #bitmask
        """
        def backtrack(i,count):
            if i == n:
                return True
            for j in count:
                if count[j]>= quantity[i]:
                    count[j] -= quantity[i]
                    res = backtrack(i+1,count)
                    count[j] += quantity[i]
                    if res:
                        return True
            return False

        n = len(quantity)
        _count = Counter(nums)
        count = Counter()
        for key in sorted(_count.keys(),key = lambda x: -_count[x]):
            count[key] = _count[key]
        quantity.sort(reverse=True)
        return backtrack(0,count)