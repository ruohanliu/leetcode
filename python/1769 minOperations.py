class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
            #dp
        """
        n = len(boxes)
        left = [0]
        cnt = 0
        for i in range(n):
            left.append(left[-1] + cnt)
            if boxes[i] == "1":
                cnt += 1
                
        right = [0]
        cnt = 0
        for i in reversed(range(n)):
            right.append(right[-1] + cnt)
            if boxes[i] == "1":
                cnt += 1
        
        return [a+b for a,b in zip(left[1:],right[1:][::-1])]