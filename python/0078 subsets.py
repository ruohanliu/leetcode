class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[x for j,x in enumerate(nums) if 1 << j & i] for i in range(2**(len(nums)))]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for x in nums:
            new = [subset+[x] for subset in res]
            res.extend(new)
        
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def add(x):
            nonlocal res
            res += [subset + [x] for subset in res]

        res = [[]]
        list(map(add,nums))
        return res