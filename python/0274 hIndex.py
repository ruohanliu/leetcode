class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
            #countsort #algorithm #google
        """
        citations.sort()
        lo = 0
        hi = citations[-1]
        n = len(citations)
        
        while lo < hi :
            mid = (lo+hi) // 2 + 1
            if n - bisect.bisect_left(citations,mid) >= mid:
                lo= mid
            else:
                hi = mid - 1
                
        return lo
        
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations) 
        # h index is at most n
        cnt = [0] * (n+1)
        for c in citations:
            cnt[min(n,c)] += 1
        
        h = n
        papers = 0 
        while True:
            papers += cnt[h]
            if papers < h:
                h -= 1
            else:
                return h
