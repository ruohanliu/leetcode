class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        """
            #edge

            set time for microwave
        """
        m,s = divmod(targetSeconds,60)
        ans1 = float("inf")
        ans2 = float("inf")
        # choice 1 ~ largest min then seconds
        if m<100:
            ans1 = 0
            fmtM = f"{m}" if m else ""
            fmtS = f"{s:0>2}" if m > 0 else str(s)
            seq = f"{fmtM}{fmtS}"
            pos = startAt
            for c in seq:
                if int(c) != pos:
                    ans1 += moveCost
                    pos = int(c)
                ans1 += pushCost
        if s<=39 and m >= 1:
            ans2 = 0
            fmtM = f"{m-1}" if m-1 else ""
            fmtS = f"{s+60:0>2}" if m-1 > 0 else str(s+60)
            seq = f"{fmtM}{fmtS}"
            pos = startAt
            for c in seq:
                if int(c) != pos:
                    ans2 += moveCost
                    pos = int(c)
                ans2 += pushCost
        return min(ans1,ans2)