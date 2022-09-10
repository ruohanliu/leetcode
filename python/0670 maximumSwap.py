class Solution:
    def maximumSwap(self, num: int) -> int:
        """
            #stack
        """
        digits = list(map(int,list(str(num))))
        n = len(digits)
        stack = []
        nextGT = [-1]*n
        for i,x in enumerate(digits):
            while stack and digits[stack[-1]] < x:
                j = stack.pop()
                nextGT[j] = i
            stack.append(i)
        for i,x in enumerate(nextGT):
            if x > -1:
                mx = float("-inf")
                options = []
                for j in range(nextGT[i],n):
                    if digits[j] > mx:
                        options = [j]
                        mx = digits[j]
                    elif digits[j] == mx:
                        options.append(j)
                mx = float("-inf")
                ans = i
                for j in options:
                    if (digits[i] - digits[j]) * 10 ** (-j) > mx:
                        mx = (digits[i] - digits[j]) * 10 ** (-j)
                        ans = j
                
                digits[i], digits[ans] = digits[ans], digits[i]
                break
        return int(''.join(map(str,digits)))