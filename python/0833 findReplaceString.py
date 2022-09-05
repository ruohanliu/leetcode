class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = []
        p = 0
        for i,f,t in sorted(zip(indices,sources,targets)):
            if i > p:
                ans.append(s[p:i])
                p = i
            if s[i:].startswith(f):
                ans.append(t)
                p = i+len(f)
        if p < len(s):
            ans.append(s[p:])
        return "".join(ans)
                
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = list(s)
        for i,f,t in zip(indices,sources,targets):
            if s.startswith(f,i):
                ans[i] = t
                for j in range(i+1,len(f)+i):
                    ans[j] = ""
        return "".join(ans)