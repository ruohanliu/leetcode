class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        """
            #rabin-karp #important #algorithm
        """
        n = len(dict)
        m = len(dict[0])
        strHash = [0]*n
        mod = 1000000007
        for i,word in enumerate(dict):
            bitmask = 0
            for c in (word):
                bitmask = (bitmask * 26 + (ord(c)-97)) % mod
            strHash[i] = bitmask
        
        mult = 1
        for j in reversed(range(m)):
            seen = defaultdict(list)
            for i,word in enumerate(dict):
                val = (strHash[i]-(ord(word[j])-97) * mult) % mod
                if val in seen:
                    if any(sum(w!=ww for w,ww in zip(word,seenWord)) == 1 for seenWord in seen[val]):
                        return True
                seen[val] += word,
            mult = (mult * 26) % mod
        return False
                
    def differByOne_tle(self, dict: List[str]) -> bool:
        """
            #trie
        """
        def search(word):
            n = len(word)
            for i in range(n):
                node = trie
                for j,c in enumerate(word):
                    if i == j:
                        for trial in node.keys():
                            if trial != c:
                                if searchSuffix(word[j+1:],node[trial]):
                                    return True
                        break
                    else:
                        if c not in node:
                            return False
                        node = node[c]
            return False
        def searchSuffix(word,node):
            for c in word:
                if c not in node:
                    return False
                node = node[c]
            return "$" in node
   
        if len(dict) < 2:
            return False

        trie = {}
        for word in dict:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["$"] = ""

        return any(search(word) for word in dict)

    def differByOne_tle(self, dict: List[str]) -> bool:
        def search(node,l):
            if l:
                return any(search(node[c],l-1) for c in node.keys())
            else:
                currKeys = list(node.keys())
                n = len(currKeys)
                for i in range(n-1):
                    for j in range(i+1,n):
                        if anyMatch(node[currKeys[i]],node[currKeys[j]]):
                            return True
                return False

        def anyMatch(n1,n2):
            if "$" in n1 and "$" in n2:
                return True
            intersection =  set(n1.keys()) & set(n2.keys())
            if not intersection:
                return False
            return any(anyMatch(n1[k],n2[k]) for k in intersection)

   
        if len(dict) < 2:
            return False

        trie = {}
        for word in dict:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["$"] = ""

        return any(search(trie,i) for i in range(len(dict[0])))