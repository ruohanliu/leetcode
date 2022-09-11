# Notes
`+`,`-` have higher precedence over `>>`, `<<`


## binary search
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
4. floating point binary search use precision ans while condition: eg. `while hi-lo > 1E-5`


## dp
optimal substructure; overlapping sub-problem
1. determine dp array meaning
2. determine dp formula
3. initialize dp array
4. determine order of traversal

## prefixsum
1. sum(i:j] can be computed  as prefixSum(j) - prefixSum(i)
2. there are n*(n+1)/2 non-empty subarrays
3. add 0 to the beginning of prefixsum

## subarray c(n+1,2) non-empty. c(n,2) multi-element 
1. kadane - can be used to find min subarray sum
    1. max sum (with one operation)
    2. max product
    3. max sum circular subarray (hard 918)
2. hash table
    1. initialization:
        1. length:{0:-1}
        2. count: {0:1}
    2. sum mod k
    3. sum == k
    4. count with more 1s than 0s 
    5. max substring without repeating char
3. sliding window
    1. min len with sum >= k (non-negative)
    2. count with sum <= k, sum == k (non-negative)
    3. count with product < k (positive)
    4. count with other subarray criteria
        1. number of unique element <= k or == k
        2. number of odd element == k (1 pass possible: 1248)
        3. contain three element (1 pass possible: 1358)
    5. string related
        1. min substring to replace to make s balaced(1234)
4. dp
    1. max len in two arrays (718)
    2. max len with positive product
    3. lcs - rabin-karp
        1. longest repeating substring
        2. can transform into lis if one of the string has all unique chars
    4. count unique/distinct char in all substrings `charLen[j] = i - charIndex[j]` `ans += sum(charLen)`(828 940)
5. mono stack
    1. sum of all subarray's min
6. deque
    1. min len with sum >= k (862)
    2. max len with (mx-mn) <= k (1438)
7. binary search
    1. max average with len >= k (644 hard)
8. local max/min point
    1. min len subarray to sort to make array sorted
    2. min len subarray to remove to make array sorted
    3. next permutation
9. heap
    1. enumerate all subarray sums in sorted order (1508)
10. set
    1. find all subarray bitwise OR values

## string rolling hash - rabin-karp
1. pick a prime: 2^61-1
2. construct base and hash array of length n+1
    1. base: [1]  [-1] * 26 % mod
    2. hash: [0]  ([-1] * 26 + ord(c) - ord("a")) % mod
3. hash for s[i:i+k] = (hash[i+k] - hash[i]*base[k]) % mod

## subsequence
1. Counter
    1. max len of harmonious subsequence (max-min == 1)
    2. split sorted array into consecutive subsequence of length >= 3
    3. max len of subsequence repeated k times in string S (2014)
2. dp
    1. count subsequence of s which equal to t   `dp(i+1,j+1) + dp(i+1,j)` `dp(i+1,j)`
    2. LCS
    3. max len of common subsequence `dp[i][j] = 1+dp[i+1][j+1]` `dp[i][j] = max(dp[i][j+1],dp[i+1][j])`
    4. max len of wiggle subsequence  `up,dn = dn+1,dn` `up,dn = up,up+1`
    5. max len of palindrome subsequence `dp[l][r] = max(dp[l+1][r],dp[l][r-1])`
    6. min len of s1 subarray, of which s2 is a subsequence (727)  `prev[0] = i+1` `curr[j+1] = prev[j]`
    7. max len and count of arithmetic subsequence `dp[j,diff] = dp[i,diff]+1`
    8. count distinct subsequence (940) `end[ord(c) - ord('a')] = sum(end) + 1`
    9. max len fibonacci subsequence `dp[j,i] = dp[idx[a],j] + 1`
    10. count LIS `dp[i] = [localMax,dp[j][1]]` `dp[i][1] += dp[j][1]`
    11. count unique subsequence of binary string `ones = (zeros + ones + 1) % mod` `zeros = (zeros + ones) % mod`  `ans = (zeros + ones) % mod`
3. index map
    1. transform lcs into lis (1713)
4. binary search
    1. LIS (300 368)
5. deque
    1. max sum where every two consecutive elements are no more than k apart. dp in decQueue. 1. use queue left, update dp 2. update queue right 3. pop queue left  (1425)
6. iter
    1. count of words which are subsequence of string S
7. bitwise
    1. max len of binary subsequence <= k
8. sliding window
    1. count where min+max == target

## subset
1. dp
    1. partition positive array into 2 substs with equal sum
    2. partition positive array into k substs with equal sum `dfs(state,target,completed)` (698)

## matrix
1. initialization use `[[0] * x for _ in range(x)]`
2. dfs/bfs record visited status early when adding to stack/queue. check validity of initial stack/queue

## Graph
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
5. Prim
    1. works for finding MST in undirected with negative weight edge
6. Kruskal
    1. undirected edge-weighted graph
7. Bellman-Ford
    1. Single source shortest path, like Dijkstra. O(VE) time complexity, works for negative weight edge.
7. BFS
    1. usually for shortest path
8. Bipartition
    1. iff the graph does not contain odd cycle
    2. sum of X degree = sum of Y degree

## Misc.
1. During recursion, when mutable type is added to answer, a copy must be created.
2. Two pointer: one pointer start at loose condition, other start at tight condition
```
i = 0
j = n-1
ans = 0
while i<j:
    if f(i,j):
        ans += j-i
        j-=1
    else:
        i+=1
```