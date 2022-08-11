class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
            #dp #game
        """
        # game() returns the score diff A-B
        @cache
        def game(lo,hi):
            if lo==hi:
                return nums[lo] 
            choiceA = nums[lo] - game(lo+1,hi)
            choiceB = nums[hi] - game(lo,hi-1)

            return max(choiceA,choiceB)
        return game(0,len(nums)-1) >=0