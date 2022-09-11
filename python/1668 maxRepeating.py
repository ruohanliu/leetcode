class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
            #rabin-karp

            O(n)
        """
        n = len(sequence)
        m = len(word)
        mod = 10**9+7
        base = [1]
        hashed = [0]
        target = []
        for c in sequence:
            base.append(base[-1]*26%mod)
            hashed.append((hashed[-1]*26+ord(c)-97)%mod)
        hashCode = 0
        for _ in range(n//m):
            for c in word:
                hashCode = (hashCode*26+ord(c)-97) % mod
            target.append(hashCode)
        repeat = 1
        for i in range(n):
            j = i+m*repeat
            if j > n:
                break
            # check current max repeat
            if (hashed[j] - hashed[i] * base[m*repeat]) % mod == target[repeat-1]:
                # if max repeat if found, move forword 1 word
                # while loop executes maximum n//m times
                while j+m <= n and (hashed[j+m] - hashed[j] * base[m]) % mod == target[0]:
                    repeat += 1
                    j+=m
                else:
                    repeat += 1
        return repeat - 1