class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
            #sort #greedy
            related 1776
        """
        cars = sorted((a,b) for a,b in zip(position,speed))
        prevTime = 0
        ans = 0
        for pos,speed in reversed(cars):
            time = (target-pos) / speed
            
            # slower than previous car
            if time > prevTime:
                ans += 1
                prevTime = time
            # collide use prevcar speed and time
        return ans