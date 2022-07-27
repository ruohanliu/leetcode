class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
            #matrix #binarysearch
        """
        m = len(mat)
        n = len(mat[0])
        
        # search by column
        lo = 0
        hi = n-1
        while lo<=hi:
            mid = (lo + hi) //2
            
            maxR = 0
            for r in range(m):
                maxR = r if mat[r][mid] >= mat[maxR][mid] else maxR
            
            if (mid<1 or mat[maxR][mid] > mat[maxR][mid-1]) and (mid==n-1 or mat[maxR][mid] > mat[maxR][mid+1]):
                return (maxR,mid)
            elif (mid>=1 and mat[maxR][mid] < mat[maxR][mid-1]):
                hi = mid-1
            else:
                lo = mid+1
