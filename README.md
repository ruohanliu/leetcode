## Notes

`+`,`-` have higher precedence over `>>`, `<<`


##### binary search
1. always use while lo < hi
2. determine which side is safe to shrink, prioritize shrinking on this side.
    1. if left is safe, then `mid = (lo + hi) // 2`
    2. if right is safe, then `mid = (lo + hi) // 2 + 1`
3. Consider corner case where length < 2


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
