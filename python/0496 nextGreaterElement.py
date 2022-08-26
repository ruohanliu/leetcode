class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            #stack #monostack #important
        """
        stack = []
        nG = defaultdict(lambda:-1)
        for y in nums2:
            while stack and stack[-1] < y:
                nG[stack.pop()] = y
            stack.append(y)
        return [nG[x] for x in nums1]