
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
            #matrix #diagonal

            diagnoal index i-j = k for 0 <= i < m and 0 <= j < n
            antidiagnoal index i+j = k for 0 <= i < m and 0 <= j < n
        """
        ans = []
        for i in reversed(range(len(nums))):
            for j,e in enumerate(nums[i]):
                while len(ans) <= i+j:
                    ans.append([])
                ans[i+j].append(e)

        return [e for d in ans for e in d]
