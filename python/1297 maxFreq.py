class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
            lee215:
                If a string have occurrences x times,
                any of its substring must appear at least x times.

                There must be a substring of length minSize, that has the most occurrences.
                So that we just need to count the occurrences of all substring with length minSize.

            #collections
            Counter.most_common()
            check if Counter is empty

            take away
                a - b is not same as a.subtract(b): a.subtract() can be negative
        """
        from collections import Counter
        c = Counter([s[i:i+minSize] for i in range(len(s)-minSize + 1) if len(set(s[i:i+minSize])) <= maxLetters])
        return c.most_common(1)[0][1] if c else 0

s = Solution()
print(s.maxFreq("abcde",2,3,3))


        