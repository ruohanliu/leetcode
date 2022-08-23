class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
            #deque #sorteddict #important #twopointer #slidingwindow

            order of subarray elements do not matter
            only compare min and max of subarray
        """
        from sortedcontainers import SortedDict
        sd = SortedDict()
        mn = float("inf")
        mx = float("-inf")
        n = len(nums) 
        i = 0
        ans = 1
        for j in range(n):
            x = nums[j]
            mn = min(mn,x)
            mx = max(mx,x)
            if x in sd:
                sd[x] += 1
            else:
                sd[x] = 1
            
            while mx-mn > limit:
                y = nums[i]
                sd[y] -= 1
                if sd[y] == 0:
                    del sd[y]
                i += 1
                mn = sd.peekitem(0)[0]
                mx = sd.peekitem(-1)[0]
            ans = max(ans,j-i+1)
        return ans
    
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mind = deque()
        maxd = deque()
        i = 0
        for x in nums:
            while maxd and x > maxd[-1]:
                maxd.pop()
            while mind and x < mind[-1]:
                mind.pop()
            maxd.append(x)
            mind.append(x)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]:
                    maxd.popleft()
                if mind[0] == nums[i]:
                    mind.popleft()
                i+=1
        return len(nums) - i