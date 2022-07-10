from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        """
            #heap #hard #important
        """
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort(key = lambda e:(e[0],-e[1],e[2]))

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, H, R in events:
            # 1, pop buildings that are already ended
            while live[0][1] <= pos:
                heappop(live)
            # 2, if it's the start-building event, make the building alive
            if H: heappush(live, (-H, R))
            # 3, if previous keypoint height != current highest height, edit the result
            if res[-1][1] != -live[0][0]:
                res.append([pos, -live[0][0]])
        return res[1:]