class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
            #optimization
            relatest 1383 maxPerformance
        """
        properties.sort(key = lambda x:(-x[1],x[0]))
        ans = 0
        maxX = properties[0][0]
        for x,_ in properties:
            if x < maxX:
                ans +=1
            else:
                maxX = x
        return ans