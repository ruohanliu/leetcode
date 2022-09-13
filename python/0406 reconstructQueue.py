class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
            #greedy #insert
        """
        people.sort(key = lambda x:(-x[0],x[1]))
        ans = []
        for h,k in people:
            ans.insert(k,[h,k])
        return ans
