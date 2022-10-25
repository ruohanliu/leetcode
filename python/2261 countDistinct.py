class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """
            #rabin-karp #trie
        """
        mod = 2**31-1
        base = [1]
        hashed = [0]
        for x in nums:
            base.append(base[-1]*200%mod)
            hashed.append((hashed[-1]*200 + x)%mod)
        i = 0
        cnt = defaultdict(set)
        for j,x in enumerate(nums):
            if x % p == 0:
                k -= 1
            while k < 0:
                if nums[i] % p == 0:
                    k += 1
                i+=1
            for s in range(i,j+1):
                cnt[j-s].add((hashed[j+1] - hashed[s]*base[j-s+1]) % mod)
        return sum(map(lambda x: len(cnt[x]),cnt))

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        i = 0
        ans = 0
        trie = {}
        for j,x in enumerate(nums):
            if x % p == 0:
                k -= 1
            while k < 0:
                if nums[i] % p == 0:
                    k += 1
                i+=1
            node = trie
            for y in reversed(nums[i:j+1]):
                if y not in node:
                    node[y] = {}
                    ans += 1
                node = node[y]
        return ans

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """
            O(n^3)
        """
        i = 0
        ans = set()
        for j,x in enumerate(nums):
            if x % p == 0:
                k -= 1
            while k < 0:
                if nums[i] % p == 0:
                    k += 1
                i+=1
            for s in range(i,j+1):
                ans.add(tuple(nums[s:j+1]))
        return len(ans)