class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
            #slidingwindow #anagram
        """
        ns = len(s)
        np = len(p)
        sc = Counter()
        pc = Counter(p)

        if ns<np:
            return []

        ans = []
        for i,c in enumerate(s):
            sc[c]+=1
            if i >= np:
                if sc[s[i-np]] == 1:
                    del sc[s[i-np]]
                else:
                    sc[s[i-np]] -=1
            
            if sc == pc:
                ans.append(i-np+1)
        return ans