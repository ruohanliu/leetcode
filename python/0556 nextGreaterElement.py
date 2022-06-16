class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
            #permutation #binarysearch
        """
        digits = [int(c) for c in str(n)]
        n = len(digits)
        for i in range(n-1, 0, -1):
            if digits[i-1] < digits[i]:
                lo = i
                hi = n-1
                while lo < hi:
                    mid = (lo+hi)//2 + 1
                    if digits[mid] > digits[i-1]:
                        lo = mid
                    else:
                        hi = mid-1
                digits[i-1], digits[lo] = digits[lo], digits[i-1]
                digits[i:] = digits[i:][::-1]
                res = 0
                p = 0
                while digits:
                    res += digits.pop() * 10**p
                    p += 1
                if res > (1 << 31) - 1:
                    return -1
                else:
                    return res
        return -1