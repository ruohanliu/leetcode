class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        """
            #bitwise
        """
        ans = set()
        visited = {0}
        for x in arr:
            visited = {x|y for y in visited} | {x}
            ans |= visited
        return len(ans)