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


##### dp
optimal substructure; overlapping sub-problem
1. determine dp array meaning
2. determine dp formula
3. initialize dp array
4. determine order of traversal

##### prefixsum
sum(i:j] can be computed  as prefixSum(j) - prefixSum(i)
initialize memo/counter


##### matrix
1. initialization use `[[0] * x for _ in range(x)]`


##### Graph
1. adjacency list use set if vertices need to be removed, such as in topological sort and dijkstra
2. Topological sort
    1. create adjList, inDegree, queue. queue should be created from all vertices instead of defaultdict
    2. if all parent of a vertext are needed, create a vertex[parents] map.  O(n^3) time and O(n^2) space
3. DAG
    1. no need to check visited vertices
4. Dijkstra
    1. use dist[].
    2. check visited status before push to heap

##### Misc.
1. During recursion, when mutable type is added to answer, a copy must be created.