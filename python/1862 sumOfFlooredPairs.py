class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        """
            #binarysearch
        """
        mod = 10**9 + 7
        count = Counter(nums)
        count = sorted([(x,count[x]) for x in count])
        ps = list(accumulate([0]+[x[1] for x in count]))
        count = [x[0] for x in count]
        n = len(count)
        ans = 0
        for i in range(n):
            denominator = count[i]
            j = 0
            k = 0
            numerator = denominator
            while numerator <= count[-1] + 1 and k < n:
                numerator = (count[k] // denominator + 1) * denominator
                k = bisect.bisect_left(count,numerator,j)
                ans += (numerator-1)//denominator * (ps[k] - ps[j]) * (ps[i+1] - ps[i])
                j = k
        return ans % mod