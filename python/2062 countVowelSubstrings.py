class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        """
            #slidingwindow
        """
        curr = Counter()
        vowel = set("aeiou")
        ans = 0
        l = 0
        r = 0
        for j,c in enumerate(word):
            if c not in vowel:
                curr.clear()
                l = j+1
                r = j+1
            else:
                curr[c] += 1
                if len(curr) == 5:
                    while curr[word[r]]>1:
                        curr[word[r]] -= 1
                        r+=1
                    ans += r-l + 1
        return ans