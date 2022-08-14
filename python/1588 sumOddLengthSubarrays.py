class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
            #contribution
        """
        ans = 0
        n = len(arr)
        for i in range(n):
            ans += (((i+1)*(n-i)+1)//2)*arr[i]
        return ans
        