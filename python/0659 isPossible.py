class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
            #heap #counter
        """
        heap = []
        for i in range(len(nums)):
            while heap and heap[0][0] < nums[i] - 1:
                _,k = heapq.heappop(heap)
                if k < 3:
                    return False
            if heap:
                if nums[i] - 1 == heap[0][0]:
                    heapq.heapreplace(heap,(heap[0][0]+1,heap[0][1]+1))
                else:
                    heapq.heappush(heap,(nums[i],1))
            else:
                heapq.heappush(heap,(nums[i],1))
        for _,k in heap:
            if k < 3:
                return False
        return True

    def isPossible(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i in c:
            while c[i] > 0:
                last = 0
                j = i
                k = 0
                while c[j] >= last:
                    last = c[j]
                    c[j] -= 1
                    j += 1
                    k += 1
                if k < 3:
                    return False
        return True