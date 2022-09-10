class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
            #heap
            related 295
            O(nlogk)
        """
        from sortedcontainers import SortedList
        window = SortedList(nums[:k])
        mid = k//2
        medians = [(window[mid] + window[~mid]) / 2]
        for a, b in zip(nums[:-k], nums[k:]):
            window.remove(a)
            window.add(b)
            medians.append((window[mid] + window[~mid]) / 2)
        return medians

    def medianSlidingWindow(self, nums, k):
        window = sorted(nums[:k])
        mid = k//2
        medians = [(window[mid] + window[~mid]) / 2]
        for a, b in zip(nums[:-k], nums[k:]):
            window.remove(a)
            bisect.insort(window, b)
            medians.append((window[mid] + window[~mid]) / 2)
        return medians