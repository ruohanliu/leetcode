class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
            #dp
        """
        @cache
        def dp(i,j):
            k = i+j
            if i == m and j == n:
                return True
            elif i == m:
                return s2[j:] == s3[k:]
            elif j == n:
                return s1[i:] == s3[k:]
            if s3[k] == s1[i]:
                if dp(i+1,j):
                    return True
            if s3[k] == s2[j]:
                if dp(i,j+1):
                    return True
            return False

        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False
        return dp(0,0)
        
        