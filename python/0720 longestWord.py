class Solution:
    def longestWord(self, words: List[str]) -> str:
        """
            #trie
        """
        ans = 0
        words = set(words)
        candidate = []
        def check(word):
            if word == "":
                return True
            if word not in words:
                return False
            return check(word[:-1])
        for word in words:
            if len(word) > ans:
                if check(word):
                    candidate = [word]
                    ans = len(word)
            elif len(word) == ans:
                if check(word):
                    candidate.append(word)
        
        return min(candidate,default = "")

    def longestWord(self, words: List[str]) -> str:
        trie = {"$":"$"}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["$"] = word
        
        def dfs(node,depth):
            nonlocal ans,maxLen
            if "$" not in node:
                return
            if depth > maxLen:
                ans = [node["$"]]
                maxLen = depth
            elif depth == maxLen > 0:
                ans.append(node["$"])
            for child in node:
                if child != "$":
                    dfs(node[child],depth + 1)

        ans = []
        maxLen = 0
        dfs(trie,0)
        return min(ans,default = "")