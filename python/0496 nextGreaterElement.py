class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            #stack #deque
        """
        stack = deque([])
        n2_dict = {}
        for n2 in nums2:
            while stack and stack[-1] < n2:
                n2_dict[stack.pop()] = n2
            stack.append(n2)
        while stack:
            n2_dict[stack.pop()] = -1
        return [n2_dict[x] for x in nums1]
                