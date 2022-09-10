class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k,points,key = lambda x:x[0]**2+x[1]**2)

    def kClosest(self, nums: List[List[int]], k: int) -> List[List[int]]:
        """
            #quickselect
        """
        def squared_distance(point) -> int:
            return point[0] ** 2 + point[1] ** 2

        def quickselect(nums,lo,hi,k):
            def partition(lo,hi):
                pivot = squared_distance(nums[random.randrange(lo,hi+1)])
                i = lo
                while i <= hi:
                    if squared_distance(nums[i]) < pivot:
                        nums[i],nums[lo] = nums[lo],nums[i]
                        lo += 1
                        i += 1
                    elif squared_distance(nums[i]) > pivot:
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

        quickselect(nums,0,len(nums)-1,k)
        return nums[:k]