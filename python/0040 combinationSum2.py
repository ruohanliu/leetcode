class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            #dfs #backtrack #duplicate
        """
        candidates.sort()
        ans = []
        def dfs(target,progress,j):
            if not target:
                ans.append(progress.copy())
                return
            for i in range(j,len(candidates)):
                c = candidates[i]
                if i > j and c == candidates[i-1]:
                    continue
                if target < c:
                    break
                if c <= target:
                    progress.append(c)
                    dfs(target-c,progress,i+1)
                    progress.pop()

        dfs(target,[],0)
        return ans