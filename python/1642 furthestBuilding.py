class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
            #binarysearch #greedy #heap

            related: 871 630
        """
        heap = []
        n = len(heights)
        for i in range(1,n):
            diff = heights[i] - heights[i-1]
            if diff>0:
                bricks -= diff
                heapq.heappush(heap,-diff)
                while bricks < 0 and heap and ladders > 0:
                    mx = -heapq.heappop(heap)
                    bricks += mx
                    ladders -= 1
                if bricks < 0:
                    return i-1
        return n-1


    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heightDiff = sorted([(y-x,i) for i,(x,y) in enumerate(zip(heights,heights[1:]))],reverse = True)
        def check(i):
            cost = 0
            ladder = ladders
            for x,j in heightDiff:
                if j < i and x > 0:
                    if ladder:
                        ladder -= 1
                    else:
                        cost += x
            return cost <= bricks
        
        lo = 0
        hi = len(heights)-1
        while lo<hi:
            mid = (lo+hi)//2 + 1
            if check(mid):
                lo = mid
            else:
                hi = mid-1
        return lo

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def solveWithGivenThreshold(K):
            """
                optimized by choosing threshold k                
            """
            
            ladders_remaining = ladders
            bricks_remaining = bricks
            ladders_used_on_threshold = 0
            
            for i in range(len(heights) - 1):
                climb = heights[i + 1] - heights[i]
                if climb <= 0:
                    continue
                    
                # Make resource allocations
                if climb == K:
                    ladders_used_on_threshold += 1
                    ladders_remaining -= 1
                elif climb > K:
                    ladders_remaining -= 1
                else:
                    bricks_remaining -= climb
                    
                # Handle negative resources.
                if ladders_remaining < 0:
                    if ladders_used_on_threshold:
                        ladders_used_on_threshold -= 1
                        ladders_remaining += 1
                        bricks_remaining -= K
                    else:
                        return [i, ladders_remaining, bricks_remaining]
                
                if bricks_remaining < 0:
                    return [i, ladders_remaining, bricks_remaining]
            
            return [len(heights) - 1, ladders_remaining, bricks_remaining]
                
        
        # Find the minimum climb and maximum climbs
        lo = math.inf
        hi = -math.inf
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            lo = min(lo, climb)
            hi = max(hi, climb)
        
        if lo == math.inf: # Was there no climbs?
            return len(heights) - 1
        
        # Carry out the binary search.
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            index_reached, ladders_remaining, bricks_remaining = solveWithGivenThreshold(mid)
            # Did we get all the way?
            if index_reached == len(heights) - 1:
                return len(heights) - 1
            # Otherwise, if we have a ladder remaining, it has to be too high.
            if ladders_remaining > 0:
                hi = mid - 1
                continue
                
            # Otherwise, check for the other optimal conditions.
            next_climb = heights[index_reached + 1] - heights[index_reached]
            if bricks_remaining < next_climb and bricks_remaining < mid:
                return index_reached
            
            # Otherwise, it must have been too low.
            lo = mid + 1