class Solution:
    def maximumSwap(self, num: int) -> int:
        """
            #digits
        """
        A = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if d in last and last[d] > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num

    def maximumSwap(self, num: int) -> int:
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