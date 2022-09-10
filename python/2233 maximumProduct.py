class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        """
            related 2333 1648
        """
        c = Counter(nums)
        n = len(c)
        keys = sorted(c.keys())
        sentinel = keys[-1]+k
        keys.append(sentinel)
        c[sentinel] = 1
        for i in range(n):
            h = keys[i]
            H = keys[i+1]
            w = c[h]
            if (H-h)*w < k:
                k -= (H-h)*w
                c[H] += w
                del c[h]
            else:
                q,m = divmod(k,w)
                c[h+q] += w-m
                c[h+q+1] += m
                c[h] -= w
                k = 0
                break
        
        c[sentinel] -= 1
        ans = 1
        mod = 10**9+7
        for x in c:
            if c[x]:
                ans = ans * pow(x,c[x],mod) % mod
        return ans

    def maximumProduct(self, nums: List[int], k: int) -> int:
        """
            related 2333 1648
        """
        n = len(nums)
        diff = sorted(nums)
        diff.append(diff[-1]+k)
        h = diff[0]
        for i in range(n):
            if h < diff[i+1]:
                if (-h + diff[i+1])*(i+1) < k:
                    k -= (-h + diff[i+1])*(i+1)
                    h = diff[i+1]
                else:
                    q,m = divmod(k,i+1)
                    h += q
                    for j in range(i+1):
                        diff[j] = h
                        if m:
                            diff[j]+=1
                            m -= 1
                    k=0
                    break
        ans = 1
        mod = 10**9+7
        for x in diff[:-1]:
            ans = (ans * x) % mod
        return ans

    def maximumProduct(self, nums: List[int], k: int) -> int:
        """
            O(KlogN)T O(N)S
        """
        heapq.heapify(nums)
        [heapq.heapreplace(nums, nums[0] + 1) for _ in range(k)]
        return functools.reduce(lambda acc, n: acc * n % (10 ** 9 + 7), nums)
