from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        """
            #kth #quickselect #algorithm #important
        """
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=lambda x : count[x]) 

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def quickselect(nums,lo,hi,k):
            def partition(lo,hi):
                pivot = count[nums[random.randrange(lo,hi+1)]]
                i = lo
                while i <= hi:
                    if count[nums[i]] < pivot:
                        nums[i],nums[lo] = nums[lo],nums[i]
                        lo += 1
                        i += 1
                    elif count[nums[i]] > pivot:
                        nums[i],nums[hi] = nums[hi],nums[i]
                        hi -= 1
                    else:
                        i += 1
                return lo,hi

            if hi <= lo:
                return
            lt,gt = partition(lo,hi)
            if lt<=k<=gt:
                return
            if k>gt:
                quickselect(nums,gt+1,hi,k)
            else:
                quickselect(nums,lo,lt-1,k)
            return

        count = Counter(nums)
        nums = list(count.keys())

        quickselect(nums,0,len(nums)-1,len(nums)-k)
        return nums[-k:]