from math import pi,atan2
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        """
            #math #pi #atan2
        """        
        arr, extra = [], 0
        xx, yy = location
        
        for x, y in points:
            if x == xx and y == yy:
                extra += 1
                continue
            arr.append(atan2(y - yy, x - xx)/pi*180)
        
        arr.sort()
        arr = arr + [x + 360 for x in arr if x < arr[-1]+angle]
        n = len(arr)
        ans = 0
        i = 0
        for j in range(n):
            while arr[j] - arr[i] > angle:
                i += 1
            ans = max(ans, j-i + 1)
            
        return ans + extra