class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        """
            #math
        """
        c = Counter(digits)
        digitSum = sum(k*c[k] for k in c)
        ans = []
        if digitSum % 3 == 1:
            if c[1] or c[4] or c[7]:
                for d in [1,4,7]:
                    if c[d]:
                        c[d]-=1
                        break
            elif c[2] + c[5] + c[8] >= 2:
                cnt = 2
                while cnt:
                    for d in [2,5,8]:
                        if c[d]:
                            c[d]-=1
                            cnt -=1
                            break
        elif digitSum % 3 == 2:
            if c[2] or c[5] or c[8]:
                for d in [2,5,8]:
                    if c[d]:
                        c[d]-=1
                        break
            elif c[1] + c[4] + c[7] >= 2:
                cnt = 2
                while cnt:
                    for d in [1,4,7]:
                        if c[d]:
                            c[d]-=1
                            cnt -=1
                            break
        for k in sorted(c,reverse=True):
            ans.extend([str(k)]*c[k])
        if ans:
            if all(d == "0" for d in ans):
                return "0"
            return "".join(ans)
        return ""

    def largestMultipleOfThree_tle(self, digits: List[int]) -> str:
        def listToInt(progress):
            ans = 0
            for x in progress:
                ans = (ans*10+x)
            return ans

        def backtrack(i,progress,val):
            nonlocal ans
            if 10 ** (len(progress) + n-i) <= ans:
                return 
            if progress and val % 3 == 0:
                ans = max(ans, listToInt(progress))
            if i == n:
                return

            progress.append(digits[i])
            backtrack(i+1,progress,val+digits[i])
            progress.pop()
            backtrack(i+1,progress,val)
                
        ans = float("-inf")
        digits.sort(reverse=True)
        n = len(digits)
        backtrack(0,[],0)
        return str(ans) if ans > float("-inf") else ""
        