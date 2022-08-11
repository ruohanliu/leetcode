class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        """
            #digit #binarysearch #math
            
            f(x) is monotonically increasing
        """
        if k == 0:
            return 5
        cnt = 1
        p = 1
        while cnt < k:
            p += 1
            cnt = cnt * 5 + 1
        
        diff = cnt - k
        while diff:
            if diff == 1:
                return 0
            diff -= 1
            cnt = (cnt-1) // 5
            q,m = divmod(diff,cnt)
            if q > 0:
                diff = m
        return 5
        