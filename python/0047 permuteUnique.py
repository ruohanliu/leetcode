class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
            #permutation
        """
        return set(map(tuple,permutations(nums)))

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(progress,c):
            if len(progress) == n:
                ans.append(progress[:])
            for k in c:
                if c[k]:
                    progress.append(k)
                    c[k] -= 1
                    backtrack(progress,c)
                    c[k]+=1
                    progress.pop()
        ans = []
        n = len(nums)
        backtrack([],Counter(nums))
        return ans