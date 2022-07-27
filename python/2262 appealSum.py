class Solution:
    def appealSum(self, s: str) -> int:
        """
            #dp #vectorization
            find the total appeal of all substring

            dp stores the appeal for substrings ending at i 
            charIndex stores the index of last appearance of each alphabet 
        """
        n = len(s)
        charIndex = [0] * 26
        total = 0
        ans = 0
        for i in range(n):
            j = ord(s[i])-97
            total, charIndex[j] = total - charIndex[j] + i+1,i+1
            ans +=total
        return ans


