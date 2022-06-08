class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
            must choose the right correction from one side
            
            take away
                slicing cannot take negative second arg s[5:-1:-1], must use s[5::-1].
                But secord arg can go beyond len(s) such as s[3:1000:1]
        """
        lo = 0
        hi = len(s)-1
        while lo < hi:
            if s[lo] != s[hi]:
                return s[lo+1:hi+1] == s[hi:lo:-1] or s[lo:hi] == s[lo:hi][::-1]
            else:
                lo +=1
                hi -=1
        return True