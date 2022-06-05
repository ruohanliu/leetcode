from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """
            #collections #Counter

            take away
                in a one-liner, if an expression is used multiple times,
                create a variable to store result for that expression
        """
        from collections import Counter
        chars_counter = Counter(chars)
        res = 0
        for word in words:
            word_counter = Counter(word)
            if all([chars_counter[c] >= word_counter[c] for c in word_counter]):
                res+=len(word)
        return res

s = Solution()
print(s.countCharacters(["cat","bt","hat","tree"],"atach"))