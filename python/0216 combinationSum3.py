class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        """
            #dfs #backtrack
        """
        def dfs(target,progress,j,remain):
            if not target:
                if remain == 0:
                    ans.append(progress.copy())
                return
            if not remain:
                return
            for i in range(j,len(candidates)):
                c = candidates[i]
                if c > target:
                    break
                progress.append(c)
                dfs(target-c,progress,i+1,remain - 1)
                progress.pop()

        candidates = [1,2,3,4,5,6,7,8,9]
        ans = []
        dfs(target,[],0,k)
        return ans