class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
            #backtrack
        """
        newDict = defaultdict(set)
        for word in wordDict:
            newDict[len(word)].add(word)
        
        @cache
        def backtrack(i):
            if i == len(s):
                return True
            for l in newDict.keys():
                if s[i:i+l] in newDict[l]:
                    if backtrack(i+l):
                        return True
            return False
        
        return backtrack(0)
                    
            