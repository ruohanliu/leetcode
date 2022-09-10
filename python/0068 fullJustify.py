class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
            #careful
        """
        def justify(words,L,leftJustify):
            def calcSpace(space,m,i,n):
                if i == n-1:
                    return ""
                return " " * (space + (1 if i<m else 0))
            if leftJustify:
                return " ".join(words) + " "*(M-L-len(words)+1)
            else:
                space,m = divmod(M-L,len(words)-1)
                return "".join(word+calcSpace(space,m,i,len(words)) for i,word in enumerate(words))
                
        n = len(words)
        M = maxWidth
        ans = []
        curr = []
        L = 0                
        for i in range(n):
            curr.append(words[i])
            L += len(words[i])
            if i == n-1 or L + len(words[i+1]) + len(curr) > M:
                ans.append(justify(curr,L,True if len(curr) == 1 or i == n-1 else False))
                curr = []
                L = 0
        return ans