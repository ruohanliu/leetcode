class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        """
            #greedy
            related 1648
        """
        n = len(nums1)
        diff = sorted([abs(a-b) for a,b in zip(nums1,nums2)],reverse=True)+[0]
        k = k1+k2
        h = diff[0]
        for i in range(n):
            if h > diff[i+1]:
                if (h - diff[i+1])*(i+1) < k:
                    k -= (h - diff[i+1])*(i+1)
                    h = diff[i+1]
                else:
                    q,m = divmod(k,i+1)
                    h -= q
                    for j in range(i+1):
                        diff[j] = h
                        if m:
                            diff[j]-=1
                            m -= 1
                    k=0
                    break
        return sum(x**2 for x in diff) if k==0 else 0
