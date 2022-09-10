class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
            #bitwise
        """
        one = two = 0
        for x in nums:
            one = ~two & (x^one)
            two = ~one & (x^two)
        return one