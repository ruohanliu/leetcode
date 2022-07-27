class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
            #binarysearch

            Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
        """
        n = len(arr)
        if n == k:
            return arr
        left = 0
        right = len(arr)-k
        while left < right:
            mid = (left+right) // 2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]