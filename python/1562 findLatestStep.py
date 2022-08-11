class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        """
            #clever
        """
        n = len(arr)
        if m == n:
            return n
        length = [0] * (n+2)
        ans = -1
        for i,pos in enumerate(arr):
            l,r = length[pos-1],length[pos+1]
            if l == m or r == m:
                ans = i
            length[pos-l] = length[pos+r] = l+r+1
        
        return ans