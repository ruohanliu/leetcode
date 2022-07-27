class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        """
            #math #bezoutsidentity #important

            gcd(0,a) = a

            while a:
                a,b = a%b,a
            return b

            sum of both jugs can count towards the target.

            Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.
        """
        if jug1Capacity > jug2Capacity:
            jug1Capacity,jug2Capacity = jug2Capacity,jug1Capacity
        
        visited = set()
        capacity = 0
        while capacity not in visited:
            visited.add(capacity)
            if targetCapacity in [(jug2Capacity - capacity) - i * jug1Capacity for i in range(-1, (jug2Capacity - capacity)//jug1Capacity +1)]:
                return True
            capacity = jug1Capacity - ((jug2Capacity - capacity) % jug1Capacity)
        return False


    def canMeasureWater_math(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        from math import gcd
        # in case jug1Capacity or jug2Capacity == 0, gcd would not work
        # if jug1Capacity == targetCapacity or jug2Capacity == targetCapacity or (jug1Capacity+jug2Capacity) == targetCapacity: return True
        return targetCapacity % gcd(jug2Capacity,jug1Capacity) == 0 and targetCapacity<=jug2Capacity+jug1Capacity:
        
