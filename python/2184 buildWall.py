class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        """
            #dp #precompute #bitmask
        """
        def row(w,mask):
            nonlocal rows
            if w == width:
                rows.append(mask)
            if w:
                mask += 1 << w-1
            for b in bricks:
                if w + b <= width:
                    row(w+b,mask)

        @cache
        def wall(h,prev):
            nonlocal rowMap
            if h == 0:
                return 1
            return sum(wall(h-1,row) for row in rowMap[prev]) % mod
            
        mod = 10**9+7
        rows = []
        row(0,0)
        rowMap = {x:[y for y in rows if not x&y] for x in rows} | {0:rows}
        return wall(height,0)