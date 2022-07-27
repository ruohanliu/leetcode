from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
            #dp
            #dfs #topdown does not require sorting
        """
        def dfs(word):
            nonlocal wordsMap
            if word not in wordsMap:
                return 0
            if wordsMap[word] > 0:
                return wordsMap[word]
            
            maxChain = 0
            for i in range(len(word)):
                predecessor = f"{word[:i]}{word[i+1:]}"
                maxChain = max(maxChain,dfs(predecessor))
            wordsMap[word] = maxChain+1
            return maxChain+1

        wordsMap = {word:0 for word in words}
        ans = 0
        for word in words:
            dfs(word)
            ans = max(ans,wordsMap[word])
        return ans

    def longestStrChain(self, words: List[str]) -> int:
        """
            #bottomup requires sorting

            dict cannot change size during its iteration
        """
        words.sort(key=len)
        wordsMap = {}
        currLenSet = set()
        ans = 0
        currLen = 0
        for word in words:
            # memory usage optimization
            if len(word) > currLen:
                for word in currLenSet:
                    del wordsMap[k]
                currLenSet.clear()
                currLen = len(word)
            maxChain = 0
            for i in range(len(word)):
                predecessor = f"{word[:i]}{word[i+1:]}"
                if predecessor in wordsMap:
                    maxChain = max(maxChain,wordsMap[predecessor])
            wordsMap[word] = maxChain+1
            ans = max(ans,wordsMap[word])
        return ans
