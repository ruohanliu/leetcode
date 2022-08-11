class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
            #dp
        """
        @cache
        def dp(i):
            if i == n:
                return 0
            
            w = 0
            h = 0
            ans = float("inf")
            while w <= shelfWidth and i < n:
                x,y = books[i]
                w += x
                h = max(h,y)
                if w <= shelfWidth:
                    ans = min(ans, h+dp(i+1))
                    i += 1
            return ans
            
        n = len(books)
        return dp(0)