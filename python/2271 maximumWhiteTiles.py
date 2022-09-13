class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        ans = 0
        tiles.sort()
        ps = [(0,0)]
        for l,r in tiles:
            if r-l+1 >= carpetLen:
                return carpetLen
            ps.append((l,ps[-1][1]+r-l+1))

        for i,(l,r) in enumerate(tiles):
            # look for the tile that covers end of carpet
            j = bisect.bisect_left(ps,(l+carpetLen,0),i+1)-1
            temp = ps[j][1]-ps[i][1] - max(tiles[j-1][1] - (l+carpetLen) + 1,0)
            ans = max(ans,temp)
        return ans