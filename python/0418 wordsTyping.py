from typing import List
from functools import cache
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # start at i-th word, return the number of rows required for 1 iteration, and the next word to use
        # either multiple rows used for 1 loop or 1 row used for multiple loops
        def dp(i):
            loop = 0
            rowUsed = 0
            while True:
                capacity = cols
                rowUsed += 1
                while capacity >= len(sentence[i]):
                    capacity -= len(sentence[i]) + 1
                    i += 1
                    if i == n:
                        loop += 1
                        i = 0
                if loop:
                    return (i,rowUsed,loop)


        n = len(sentence)
        for word in sentence:
            if len(word) > cols:
                return 0

        ans = 0
        i = 0
        record = {}
        while rows > 0:
            record[i] = (rows,ans)
            i,rowUsed,loop = dp(i)
            if rows >= rowUsed:
                ans += loop
            rows -= rowUsed
            if rows > 0 and i in record:
                q,_ = divmod(rows,record[i][0] - rows)
                rows -= (record[i][0] - rows) * q
                ans += (ans - record[i][1]) * q
        return ans