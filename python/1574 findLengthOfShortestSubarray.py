class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
            #lis #clever
            related 300
            O(n)
        """
        n = len(arr)
        j = n-1
        while j > 0 and arr[j-1]<=arr[j]:
            j-=1
        
        ans = j
        i = 0
        while i < j and (i == 0 or arr[i-1] <= arr[i]):
            while j < n  and arr[i] > arr[j]:
                j += 1
            ans = min(ans,j-i-1)
            i += 1
        return ans