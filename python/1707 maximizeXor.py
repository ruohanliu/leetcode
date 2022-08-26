class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
            #trie #bitwise #xor
            related 421
        """
        nums.sort()
        queries = sorted([(m,x,i) for i,(x,m) in enumerate(queries)])

        L = 32
        trie = {}
        ans = [-1] * len(queries)
        i = 0
        for m,x,idx in queries:
            while i < len(nums) and nums[i] <= m:
                node = trie
                for k in reversed(range(L)):
                    bit = (nums[i] >> k) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]
                i+= 1

            if trie:
                res = 0
                node = trie
                for k in reversed(range(L)):
                    bit = (x >> k) & 1
                    rbit = 1-bit
                    res <<= 1
                    if rbit in node:
                        res += 1
                        node = node[rbit]
                    else:
                        node = node[bit]

                ans[idx] = res
        return ans