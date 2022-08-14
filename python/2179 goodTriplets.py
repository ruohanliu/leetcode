class Solution:
    def goodTriplets_mle(self, nums1: List[int], nums2: List[int]) -> int:
        return len(set((x,y,z) for x,y,z in itertools.combinations(nums1,3)) & set((x,y,z) for x,y,z in itertools.combinations(nums2,3)))

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
            #fenwicktree #bit #important
            for a given element a:
                How many elements on a's left in both A and B;
                How many elements on a's right in both A and B;

            related 315
        """
        def add(i,delta):
            i = i + 1
            while i < n+1:
                bit[i] += delta
                i += i&-i

        def query(i):
            res = 0
            i = i + 1
            while i:
                res += bit[i]
                i -= i&-i
            return res

        n = len(nums1)
        # stores number of elements that are smaller at any index for both
        bit = [0] * (n+1)
        ans = 0

        # stores index of element in nums2
        reverseNums2 = [0] * n
        for i in range(n):
            reverseNums2[nums2[i]] = i
        for i in range(n):
            # index in nums2
            idx = reverseNums2[nums1[i]]
            # smaller: number of smaller elements on the left side
            smaller = query(idx)
            # n-idx-1: number of elements on the right side of nums2[idx]
            # i-smaller: number of larger elements on the left side
            larger = n - idx - 1 - (i-smaller)
            ans += smaller * larger
            add(idx,1)
        return ans