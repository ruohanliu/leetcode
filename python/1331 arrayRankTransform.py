from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
            use len as rank value
            #rank
        """
        rank_dict = {}
        for item in sorted(arr):
            if item not in rank_dict:
                rank_dict[item] = len(rank_dict) + 1

        return [rank_dict[item] for item in arr]
            
            
        