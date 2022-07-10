class Solution:
    def longestWord(self, words: List[str]) -> str:
        """
            #trie #dfs
        """
        trie = {"$":None}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["$"] = None
        
        def dfs(node,level,chars):
            nonlocal ans,cnt
            if "$" in node:
                level += 1
                if level > cnt or (level==cnt and chars<ans):
                    cnt = level
                    ans = chars[::]
                for c in node:
                    if c != "$":
                        chars.append(c)
                        dfs(node[c],level,chars)
                        chars.pop()
        ans = []
        cnt = 0
        dfs(trie,0,[])
        
        return "".join(ans)
                
        
