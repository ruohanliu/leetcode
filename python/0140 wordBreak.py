class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
            #backtrack #important
        """
        def backtrack(i,progress):
            if i == len(s):
                ans.append(" ".join(progress))
                return
            for l in newDict.keys():
                if i+l <= len(s) and s[i:i+l] in newDict[l]:
                    progress.append(s[i:i+l])
                    backtrack(i+l,progress)
                    progress.pop()

        newDict = defaultdict(set)
        for word in wordDict:
            newDict[len(word)].add(word)

        ans = []
        backtrack(0,[])
        return ans
        