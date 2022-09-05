class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        """
            #greedy
        """
        peaks = sorted([(x-y,x+y) for x,y in peaks])
        left,right = peaks[0]
        n = len(peaks)
        ans = 0
        visible = True
        for i in range(1,n):
            _left,_right = peaks[i]
            if left == _left and right == _right:
                visible = False
                continue
            if _right > right:
                if visible and _left> left:
                    ans += 1
                left,right = _left,_right
                visible = True
        if visible:
            ans += 1
        return ans
                