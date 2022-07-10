## Notes
`+`,`-` have higher precedence over `>>`, `<<`


##### binary search
1. use `while lo < hi` if want to find index
    1. determine which side is safe to shrink, prioritize shrinking on this side.
        1. if left is safe, then `mid = (lo + hi) // 2`
        2. if right is safe, then `mid = (lo + hi) // 2 + 1`
    2. Consider corner case where length < 2
    3. resulting lo/hi is the best index satisfying the non-safer condition
2. use `while lo <= hi` if may want to return index during search
    1. mid must be `mid = (lo + hi) //2`
    2. if not returning, it must shrink on both side
3. bisect_left(nums,target) == bisect_right(nums,target) means target is not in nums


##### dp
optimal substructure; overlapping sub-problem
1. determine dp array meaning
2. determine dp formula
3. initialize dp array
4. determine order of traversal

##### prefixsum
1. sum(i:j] can be computed  as prefixSum(j) - prefixSum(i)
2. there are n*(n+1)/2 non-empty subarrays
3. add 0 to the beginning of prefixsum


##### matrix
1. initialization use `[[0] * x for _ in range(x)]`
2. dfs/bfs record visited status early when adding to stack/queue. check validity of initial stack/queue

##### Graph
1. Adjacency list use set if vertices need to be removed, such as in topological sort and dijkstra
2. Topological sort
    1. create adjList, inDegree, queue. queue should be created from all vertices instead of defaultdict
    2. if all parent of a vertext are needed, create a vertex[parents] map.  O(n^3) time and O(n^2) space
3. DAG
    1. no need to check visited vertices
    2. reversal of all edge direction does not matter
4. Dijkstra
    1. use dist[] adjList{} heap
    2. check visited status before push to heap
    3. check vertex doneness right after heappop
    4. The maximum number of vertices that could be added to the heap is E. V^2 >= E >= V-1 graph. O(E * log|V|) + O(V * logV) = O(E * logV)
    5. works for finding paths in connected non-negative directed and undirected graph
5. Kruskal
    1. undirected edge-weighted graph
6. BFS
    1. usually for shortest path
7. Bipartition
    1. iff the graph does not contain odd cycle
    2. sum of X degree = sum of Y degree

##### Misc.
1. During recursion, when mutable type is added to answer, a copy must be created.