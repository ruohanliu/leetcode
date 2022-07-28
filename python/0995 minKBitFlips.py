class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """
            #xor #greedy #deque

            order of flip does not matter. go greedy, flip whenever needed and the result is correct
        """
        n = len(nums)
        ans = 0
        queue = deque()
        for i in range(n):
            if (nums[i] + len(queue)) % 2 == 0:
                queue.append(i+k-1)
                ans += 1
                if i + k -1 >= n:
                    return -1
            if queue and queue[0] == i:
                queue.popleft()
        return ans

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """
            space optimized
        """
        n = len(nums)
        ans = 0
        curr = 0
        for i in range(n):
            if (nums[i] + curr) % 2 == 0:
                curr += 1
                ans += 1
                if i + k - 1 >= n:
                    return -1
                nums[i+k-1] += 2
            if i >= k-1 and nums[i] > 1:
                curr -= 1
                nums[i] -=2
        return ans

    def minKBitFlips_naive(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                ans += 1
                if i + k > n:
                    return -1
                for j in range(i,i+k):
                    nums[j] ^= 1
        
        return ans