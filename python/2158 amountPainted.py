class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        """
            #interval #segmenttree

            cant sort because input is ordered
        """


    def amountPainted_jumpline(self, paint: List[List[int]]) -> List[int]:
        n = len(paint)
        line = [0]*50001
        ans = [0] * n
        for i,(a,b) in enumerate(paint):
            j = a
            curr = 0
            while j < b:
                if line[j]:
                    j = line[j]
                else:
                    line[j] = b
                    j+=1
                    curr +=1
            ans[i] = curr
        return ans