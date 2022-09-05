class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        """
            #astar #bfs
        """
        # this function checks whether the given coordinates/indices are valid to go
        def valid(x,y):
            return m>x>=0<=y<n and grid[x][y]!='#'

        # this function checks whether the person can travel from current position to the destination position.
        # used simple bfs(dfs can also be used here), should be self explainatory if you know BFS.
        def travel(curr,dest,box):
            queue = deque([curr])
            v = set()
            while queue:
                pos = queue.popleft()
                if pos == dest: return True
                new_pos = [(pos[0]+1,pos[1]),(pos[0]-1,pos[1]),(pos[0],pos[1]+1),(pos[0],pos[1]-1)]
                for x,y in new_pos:
                    if valid(x,y) and (x,y) not in v and (x,y)!=box:
                        v.add((x,y))
                        queue.append((x,y))
            return False

        def heuristic(box,target):
            return abs(box[0]-target[0]) + abs(box[1]-target[1])

        m = len(grid)
        n = len(grid[0])
        # this loop is to get the coordinates of target, box and person. Nothing else is gained here
        for i,j in product(range(m),range(n)):
            if grid[i][j] == "T":
                target = (i,j)
            if grid[i][j] == "B":
                box = (i,j)
            if grid[i][j] == "S":
                person = (i,j)
        state = defaultdict(lambda:float("inf"))
        state[box+person] = 0
        heap = [(heuristic(box,target),0,box,person)]
        # this is the main bfs which gives us the answer
        while heap:
            _, steps, box, person = heapq.heappop(heap)
            if box == target: # return the distance if box is at the target
                return steps

            if not ((valid(box[0]+1,box[1]) and valid(box[0]-1,box[1])) or (valid(box[0],box[1]+1) and valid(box[0],box[1]-1))):
                continue
            #these are the new possible coordinates/indices box can be placed in (up, down, right, left).
            b_coord = [(box[0]+1,box[1]),(box[0]-1,box[1]),(box[0],box[1]+1),(box[0],box[1]-1)]
            #these are the corresponding coordinates the person has to be in to push .. the box into the new coordinates
            p_coord = [(box[0]-1,box[1]),(box[0]+1,box[1]),(box[0],box[1]-1),(box[0],box[1]+1)]

            for new_box,new_person in zip(b_coord,p_coord): 
                # we check if the new box coordinates are valid and our current state is not in visited
                # we check corresponding person coordinates are valid and if it is possible for the person to reach the new coordinates
                if steps+1 < state[new_box+box] and valid(*new_box) and valid(*new_person) and travel(person,new_person,box):
                    state[new_box+box] = steps+1
                    heapq.heappush(heap,(heuristic(new_box,target)+steps+1,steps+1,new_box,box))
        return -1