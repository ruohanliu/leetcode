class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m = len(image)
        n = len(image[0])
        
        lo = 0
        hi = x
        while lo < hi:
            mid = (lo+hi) // 2
            if any(image[mid][c] == "1" for c in range(n)):
                hi = mid
            else:
                lo = mid + 1
        upperRow = lo
        lo = x
        hi = m-1
        while lo < hi:
            mid = (lo+hi) // 2 + 1
            if any(image[mid][c] == "1" for c in range(n)):
                lo = mid
            else:
                hi = mid - 1
        lowerRow = lo

        lo = 0
        hi = y
        while lo < hi:
            mid = (lo+hi) // 2
            if any(image[r][mid] == "1" for r in range(m)):
                hi = mid
            else:
                lo = mid + 1
        leftCol = lo
        lo = y
        hi = n-1
        while lo < hi:
            mid = (lo+hi) // 2 + 1
            if any(image[r][mid] == "1" for r in range(m)):
                lo = mid
            else:
                hi = mid - 1
        rightCol = lo

        return (lowerRow - upperRow + 1) * (rightCol - leftCol + 1)