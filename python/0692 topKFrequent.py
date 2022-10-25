class Solution:
    def topKFrequent(self, nums: List[str], k: int) -> List[str]:
        """
            #quickselect
        """
        def quickselect(nums,lo,hi,k):
            def partition(lo,hi):
                key = nums[random.randrange(lo,hi+1)]
                pivot = (-count[key],key)
                i = lo
                while i <= hi:
                    if (-count[nums[i]],nums[i]) < pivot:
                        nums[i],nums[lo] = nums[lo],nums[i]
                        lo += 1
                        i += 1
                    elif (-count[nums[i]],nums[i]) > pivot:
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

        quickselect(nums,0,len(nums)-1,k)
        return sorted(nums[:k],key = lambda x: (-count[x],x))