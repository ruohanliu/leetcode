class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
            #dfs
        """
        c = Counter(letters)
        values = []
        for word in words:
            w = Counter(word)
            if c>=w:
                values.append((w,sum(w[x]*score[ord(x)-97] for x in w)))
        n = len(values)
        def dfs(i,c):
            if i == n or not c:
                return 0
            if c>=values[i][0]:
                return max(values[i][1]+dfs(i+1,c-values[i][0]),dfs(i+1,c))
            else:
                return dfs(i+1,c)
        return dfs(0,c)