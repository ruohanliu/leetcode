class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
            #dp #vectorization #important #contribution

            related: 940 2262

            find the total # of unique chars of all substring

            dp stores the appeal for substrings ending at i 
            charIndex stores the index of last appearance of each alphabet 
            sum # of unique char in all substring
        """
        # dp[i] denotes the result for substring ending at i
        n = len(s)
        # index of last time char appears
        charIndex = [-1] * 26
        # number of substring for each unique char
        charLen = [0] * 26
        ans = 0
        # for each substring ending at i
        for i in range(n):
            j = ord(s[i])-65
            charLen[j] = i - charIndex[j]
            charIndex[j] = i
            ans += sum(charLen)
        return ans

    def uniqueLetterString(self, s: str) -> int:
        # dp[i] denotes the result for substring ending at i
        n = len(s)
        charIndex = [-1] * 26
        charLen = [0] * 26
        ans = 0
        total = 0
        for i in range(n):
            j = ord(s[i])-65
            total, charLen[j] = total + i - charIndex[j] - charLen[j], i - charIndex[j]
            charIndex[j] = i
            ans += total
        return ans
