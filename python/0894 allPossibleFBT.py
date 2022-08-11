class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """
            #dp #tree
        """
        @cache
        def dp(i):
            if i == 0:
                return []
            if i == 1:
                return [TreeNode()]
            ans = []
            for j in range(1,i-1):
                leftSize = j
                rightSize = i-j-1
                for lst in dp(leftSize):
                    for rst in dp(rightSize):
                        ans.append(TreeNode(0,lst,rst))
            return ans
        return dp(n)