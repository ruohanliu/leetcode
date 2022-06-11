## Notes

`+`,`-` have higher precedence over `>>`, `<<`


###### binary search
1. always use while lo < hi
2. determine which side is safe to shrink, prioritize shrinking on this side.
    1. if left is safe, then mid = (lo + hi) // 2
    2. if right is safe, then mid = (lo + hi) // 2 + 1
3. Consider corner case where length < 2