class Solution:
    def nextPalindrome(self, num: str) -> str:
        """
            #palindrome

            related 556
        """
        s = list(num[:len(num)//2])
        n = len(s)
        
        res = ""
        for i in range(n-1,0,-1):
            if s[i-1]<s[i]:
                lo = i
                hi = n-1
                while lo<hi:
                    j = (lo+hi) //2 + 1
                    # find a j where s[j] just larger than s[i-1]
                    if s[j]<=s[i-1]:
                        hi = j-1
                    else:
                        lo = j
                s[i-1],s[lo] = s[lo],s[i-1]
                s[i:] = sorted(s[i:])
                res = "".join(s)
                break

        if not res:
            return ""
        if len(num) % 2:
            return res+num[len(num)//2]+res[::-1]
        else:
            return res+res[::-1]
