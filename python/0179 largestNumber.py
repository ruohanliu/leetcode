class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
            #customsort #important
            #functools
        """
        def cmp(x, y):
            if f"{x}{y}">f"{y}{x}":
                return 1
            elif f"{x}{y}"<f"{y}{x}":
                return -1
            else:
                return 0
        ans = "".join(map(str,sorted(nums, key=functools.cmp_to_key(cmp),reverse=True)))
        return "0" if ans[0] == "0" else ans