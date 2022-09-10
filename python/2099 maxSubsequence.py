class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
            #heap

            minheap pops the smallest number, while fixed size minheap keeps the largest k numbers.
        """
        heap = []
        for n in nums:
            if len(heap)<k:
                heapq.heappush(heap,n)
            else:
                heapq.heappushpop(heap,n)
        
        c = Counter(heap)
        ans = []
        for n in nums:
            if c[n] > 0:
                ans.append(n)
                c[n] -=1
        return ans

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
            #quickselect
        """
        def quickselect(lo,hi,k):
            def partition(lo,hi):
                i=lo
                pivot = nums[random.randrange(lo,hi+1)]
                while i <= hi:
                    if nums[i] < pivot:
                        nums[i],nums[lo] = nums[lo],nums[i]
                        i+=1
                        lo+=1
                    elif nums[i]> pivot:
                        nums[i],nums[hi] = nums[hi],nums[i]
                        hi-=1
                    else:
                        i+=1
                return lo,hi
                
            if lo>=hi:
                return
            lt,gt = partition(lo,hi)
            # quicksort variant:
            # quickselect(gt+1,hi)
            # quickselect(lo,lt-1)
            if lt<=k<=gt:
                return
            if k>gt:
                quickselect(gt+1,hi,k)
            else:
                quickselect(lo,lt-1,k)

        orig = nums[:]
        quickselect(0,len(nums)-1,len(nums)-k)
        
        c = Counter(nums[-k:])
        ans = []
        for x in orig:
            if c[x]:
                ans.append(x)
                c[x] -= 1
        return ans
