class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
            #rabin-karp

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

            O(minSize*n)
        """
        from collections import Counter
        c = Counter([s[i:i+minSize] for i in range(len(s)-minSize + 1) if len(set(s[i:i+minSize])) <= maxLetters])
        return c.most_common(1)[0][1] if c else 0

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        mod = 2**61-1
        base = 26**minSize%mod
        hashed = [0]
        hashCount = Counter()
        letterCount = Counter()
        for i,c in enumerate(s):
            letterCount[c] += 1
            hashed.append((hashed[-1]*26 + ord(c) - 97)%mod)
            if i >= minSize - 1:
                if len(letterCount) <= maxLetters:
                    hashCount[(hashed[-1] - hashed[-1-minSize]*base) % mod] += 1
                
                o = s[i - minSize + 1]
                letterCount[o] -= 1
                if letterCount[o] == 0:
                    del letterCount[o]
        return max(hashCount.values(), default=0)