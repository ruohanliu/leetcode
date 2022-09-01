class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
            #stack
        """
        ans = [0] * n
        stack = []
        for log in logs:
            i,status,time = log.split(":")
            if status == "start":
                stack.append((int(i),int(time)))
            else:
                _,startTime = stack.pop()
                latest = int(time)-startTime + 1
                ans[int(i)] += latest
                if stack:
                    i,time = stack[-1]
                    ans[i] -= latest
        return ans
            