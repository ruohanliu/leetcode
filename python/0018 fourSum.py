class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            #important
        """
        ans = []
        freq = defaultdict(list)
        n = len(nums)
        nums.sort()
        for bc in range(n-1):
            mid = nums[bc]
            
            # bc serves as c
            for d in range(bc+1, n):
                if d > bc+1 and nums[d] == nums[d-1]:
                    continue
                for a,b in freq[target - nums[d] - mid]:
                    ans.append(tuple([a,b,mid,nums[d]]))
            
            # bc serves as b
            for a in range(bc):
                if a>0 and nums[a] == nums[a-1]:
                    continue
                freq[nums[a] + mid] += (nums[a],mid),
        return set(ans)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
                return
            if N == 2:
                i,j = l,r
                while i < j:
                    if nums[i] + nums[j] < target:
                        i += 1
                    elif nums[i] + nums[j] > target:
                        j -= 1
                    else:
                        results.append(result + [nums[i], nums[j]])
                        while i < j and nums[i] == nums[i+1]:
                            i += 1
                        while j > i and nums[j] == nums[j-1]:
                            j -= 1
                        i += 1
                        j -= 1
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or nums[i-1] != nums[i]:
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results

    def twoSum(self, nums, lo,hi,target: int):
        """
        nums is sorted
        """

        ans = []
        i = lo
        j = hi
        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                ans.append((-target,nums[i],nums[j]))
                while i < hi and nums[i] == nums[i+1]:
                    i += 1
                while j > lo and nums[j] == nums[j-1]:
                    j -= 1
                i += 1
                j -= 1
        return ans


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums) - 2:
            if nums[i] > 0: break
            ans += self.twoSum(nums,i+1,len(nums) - 1,0-nums[i])
            while i < len(nums) - 2 and nums[i] == nums[i+1]:
                i+=1
            i += 1
        return ans