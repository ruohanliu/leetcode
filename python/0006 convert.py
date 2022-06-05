class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
            take away:
                itertools chain(*iterable) chain.from_iterable(iterable)
                operator module
                functools reduce

                matrix init [[]] * n does not work, use [[] for i in range(n)]
        """
        from math import ceil
        from itertools import chain
        from functools import reduce
        from operator import add
        if numRows == 1:
            return s
        ans = [[] for i in range(numRows)]
        n_char = 2 * numRows -2

        le = len(s)
        for i,c in enumerate(s):
            m = ceil(i / n_char)
            n = i % n_char
            r = n if n < numRows else 2 * numRows - n - 2
            ans[r].append(c)
        # return "".join(chain.from_iterable(ans))
        return "".join(reduce(add,ans))

s = Solution()
print(s.convert("PAYPALISHIRING",3))
