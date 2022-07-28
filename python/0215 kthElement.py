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
    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[k-1]

    # python built-in heapq
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        res = heapq.nlargest(k,nums)
        return res[k-1]

    def findKthLargest_heap2(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            if len(h) == k:
                heapq.heappushpop(h,num)
            else:
                heapq.heappush(h,num)
        return heapq.heappop(h)

    def findKthLargest_heap3(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

    def findKthLargest_heap4(self, nums: List[int], k: int) -> int:
        h = minHeap(k)
        for num in nums:
            h.push(num)
        return h.pop()

    # 3-way quick sort
    def findKthLargest_quick_sort(self, nums: List[int]) -> int:
        def quick_sort(lo,hi):
            if hi <= lo:
                return
            lt,i,gt = lo,lo+1,hi
            pivotIndex = random.randrange(lo,hi+1,1)
            nums[lo],nums[pivotIndex] = nums[pivotIndex],nums[lo]
            pivot = nums[lo]
            while i <= gt:
                if nums[i] < pivot:
                    nums[i],nums[lt] = nums[lt],nums[i]
                    lt += 1
                    i += 1
                elif nums[i] == pivot:
                    i += 1
                else:
                    nums[i],nums[gt] = nums[gt],nums[i]
                    gt -= 1
            quick_sort(lo,lt-1)
            quick_sort(gt+1,hi)

        return quick_sort(0,len(nums)-1)

    # 3-way quick select
    def findKthLargest_quick_select(self, nums: List[int], k: int) -> int:
        def partition(lo,hi):
            lt,i,gt = lo,lo+1,hi
            pivotIndex = random.randrange(lo,hi+1,1)
            nums[lo],nums[pivotIndex] = nums[pivotIndex],nums[lo]
            pivot = nums[lo]

            while i <= gt:
                if nums[i] < pivot:
                    nums[i],nums[lt] = nums[lt],nums[i]
                    lt += 1
                    i += 1
                elif nums[i] == pivot:
                    i += 1
                else:
                    nums[i],nums[gt] = nums[gt],nums[i]
                    gt -= 1
            return (lt,gt)

        def quick_select(lo,hi,k_smallest):
            if hi <= lo:
                return nums[lo]
            lt,gt = partition(lo,hi)
            if k_smallest >= lt and k_smallest <= gt:
                return nums[k_smallest]
            elif k_smallest < lt:
                return quick_select(lo,lt-1,k_smallest)
            else:
                return quick_select(gt+1,hi,k_smallest)

        return quick_select(0,len(nums)-1,len(nums)-k)


s = Solution()
print(s.findKthLargest_quick_select([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6],2))
