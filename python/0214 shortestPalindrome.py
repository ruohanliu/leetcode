class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
            #KMP #algorithm #furtherstudy
            You are given a string s. You can convert s to a palindrome by adding characters in front of it.
            Return the shortest palindrome you can find by performing this transformation.
        """
        n = len(s)
        hi = n//2

        if n <= 1:
            return s

        for mid in reversed(range(hi+1)):
            if s[:mid][::-1] == s[mid+1:2*mid+1]:
                return s[mid+1:][::-1]+s[mid:]
            elif mid > 0 and s[mid] == s[mid-1] and s[:mid-1][::-1] == s[mid+1:2*mid]:
                return s[mid:][::-1]+s[mid:]

    def shortestPalindrome(self, s: str) -> str:
        """
            #palindrome
            startswith()
            if a string startswith the reverse of it, it is a palindrome
        """
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s