class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
            #bitwise #xor #important #trie
            related 1707
        """
        L = max(nums).bit_length()
        ans = 0
        for i in reversed(range(L)):
            ans <<= 1
            curr = ans + 1
            prefixes = {num >> i for num in nums}
            # is there a prefix p such that curr^p is also in prefixes
            # p^curr^p = curr -> there are two distinct prefixes whose xor is curr
            if any(curr^p in prefixes for p in prefixes):
                ans = curr
        return ans

    def findMaximumXOR(self, nums: List[int]) -> int:
        L = max(nums).bit_length()
        nums = [[(x >> i) & 1 for i in reversed(range(L))] for x in nums]
        ans = 0
        trie = {}
        for num in nums:
            node = trie
            matched = trie
            curr = 0
            for bit in num:
                if not bit in node:
                    node[bit] = {}
                node = node[bit]
                
                rbit = 1-bit
                curr <<= 1
                if rbit in matched:
                    curr += 1
                    matched = matched[rbit]
                else:
                    matched = matched[bit]
                    
                    
            ans = max(ans,curr)
        return ans