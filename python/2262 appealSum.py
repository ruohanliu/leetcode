class Solution:
    def appealSum(self, s: str) -> int:
        """
            #dp #vectorization

            related: 828 940

            find the total appeal of all substring

            dp stores the appeal for substrings ending at i 
            charIndex stores the index of last appearance of each alphabet 
        """
        n = len(s)
        charLen = [0] * 26
        total = 0
        ans = 0
        for i in range(n):
            j = ord(s[i])-97
            total, charLen[j] = total - charLen[j] + i+1,i+1
            ans += total
        return ans

    def appealSum(self, s: str) -> int:
        n = len(s)
        charLen = [0] * 26
        ans = 0
        for i in range(n):
            j = ord(s[i])-97
            charLen[j] = i+1
            ans += sum(charLen)
        return ans