class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        """
            #stack #greedy #hard
            related 853

            Imagine a,b,c on the road
            if a catches b later than b catched c, then a won't catch b but c.
        """
        n = len(cars)
        ans = [-1] * n
        stack = []
        # cars are sorted by positions
        for i in reversed(range(n)):
            pos,speed = cars[i]
            # maintain decreasing stack of collision time
            # pop stack if current catching up time is larger (or infinity)
            while stack:
                _pos,_speed = cars[stack[-1]]
                if speed <= _speed or (_pos-pos) / (speed - _speed) >= ans[stack[-1]] > -1:
                    stack.pop()
                else:
                    break
            # cars on the stack has a strictly larger collision time, so that current car can catch up then maintain slower speed
            if stack:
                _pos,_speed = cars[stack[-1]]
                ans[i] = (_pos - pos) / (speed - _speed)
            
            # push current smaller time onto stack
            stack.append(i)
        return ans