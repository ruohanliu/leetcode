class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(target,progress,j):
            if not target:
                ans.append(progress.copy())
                return
            for i in range(j,len(candidates)):
                c = candidates[i]
                if c <= target:
                    progress.append(c)
                    dfs(target-c,progress,i)
                    progress.pop()

        dfs(target,[],0)
        return ans