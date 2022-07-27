from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(sorted(col) != list(col) for col in zip(*strs))

    def minDeletionSize(self, strs: List[str]) -> int:
        """
            #zip
        """
        return sum(any(a>b for a,b in zip(col,col[1:])) for col in zip(*strs))
