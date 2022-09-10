from typing import List
import heapq
import random
class minHeap():
    def __init__(self,maxSize:int):
        self.heap = [0]
        self.maxSize = maxSize


    def push(self,n:int):
        self.heap.append(-n)
        self.swim(len(self.heap)-1)
        if len(self.heap) - 1 > self.maxSize:
            self.pop()

    def pop(self) -> int:
        res = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.sink(1)
        return -res

    def exch(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def swim(self,i:int):
        while (i > 1 and self.heap[i]>self.heap[i//2]):
            self.exch(i,i//2)
            i //= 2

    def sink(self,i:int):
        while (2*i < len(self.heap)):
            j = 2*i
            if j+1 < len(self.heap) and self.heap[j+1]>self.heap[j]:
                j += 1
            if self.heap[i] < self.heap[j]:
                self.exch(i,j)
                i = j
            else:
                break


class Solution:
    """
        #quickselect
    """
    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[k-1]

    # python built-in heapq
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        res = heapq.nlargest(k,nums)
        return res[k-1]

    def findKthLargest_heap2(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) == k:
                heapq.heappushpop(heap,num)
            else:
                heapq.heappush(heap,num)
        return heapq.heappop(heap)

    def findKthLargest_heap3(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

    def findKthLargest_heap4(self, nums: List[int], k: int) -> int:
        heap = minHeap(k)
        for num in nums:
            heap.push(num)
        return heap.pop()

    # 3-way quick sort
    def findKthLargest_quicksort(self, nums: List[int]) -> int:
        def quicksort(nums,lo,hi):
            def partition(lo,hi):
                pivot = nums[random.randrange(lo,hi+1)]
                i = lo
                while i <= hi:
                    if nums[i] < pivot:
                        nums[i],nums[lo] = nums[lo],nums[i]
                        lo += 1
                        i += 1
                    elif nums[i] > pivot:
                        nums[i],nums[hi] = nums[hi],nums[i]
                        hi -= 1
                    else:
                        i += 1
                return lo,hi

            if hi <= lo:
                return
            lt,gt = partition(lo,hi)
            quicksort(nums,lo,lt-1)
            quicksort(nums,gt+1,hi)

        quicksort(nums,0,len(nums)-1)
        return nums[-k]

    # 3-way quick select
    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
        def quickselect(nums,lo,hi,k):
            def partition(lo,hi):
                pivot = nums[random.randrange(lo,hi+1)]
                i = lo
                while i <= hi:
                    if nums[i] < pivot:
                        nums[i],nums[lo] = nums[lo],nums[i]
                        lo += 1
                        i += 1
                    elif nums[i] > pivot:
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

        quickselect(nums,0,len(nums)-1,len(nums)-k)
        return nums[-k]
