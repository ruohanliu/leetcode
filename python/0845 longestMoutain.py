from typing import List
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
            #arrayend
        """
        n_inc = 0
        n_dec = 0
        ans = 0
        for i in range(1,len(arr)):
            if n_dec == 0 and arr[i] > arr[i-1]:
                n_inc += 1
            elif n_inc > 0 and arr[i] < arr[i-1]:
                n_dec += 1
            else:
                if n_inc > 0 and n_dec > 0:
                    ans = max(ans,n_inc+n_dec+1)
                if arr[i-1] < arr[i]:
                    n_inc = 1
                else:                    
                    n_inc = 0
                n_dec = 0
            if i == len(arr)-1 and n_inc > 0 and n_dec > 0:
                ans = max(ans,n_inc+n_dec+1)
        return ans

s = Solution()
print(s.longestMountain([875,884,239,731,723,685]))