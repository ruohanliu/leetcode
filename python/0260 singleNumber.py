class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
            #bitwise #important

            x&(-x) retains least significant 1 without shifting
            x&(x-1) gets rid of least significant 1 without shifting
        """
        xy = reduce(xor,nums)
        
        # get least significant 1 in xy, which must not be in either x or y
        diff = xy & (-xy)
        
        x_or_y = 0
        for z in nums:
            # filter out one of x and y
            if z & diff:
                x_or_y ^= z
                
        return [x_or_y,xy^x_or_y]