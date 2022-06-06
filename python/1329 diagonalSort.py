from typing import List
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
            #matrix #diagonal #sort #heap #countingsort #important

            matrix m/n definition does not matter
            matrix elements with same i-j are on the same diagonal

                n, m = len(A), len(A[0])
                d = collections.defaultdict(list)
                for i in xrange(n):
                    for j in xrange(m):
                        d[i - j].append(A[i][j])

            use count sort when value range k is ~ n. result is O(k + n)
            if exact range of value is not known, sort Counter keys. result is O(klogk + n)
        """
        import heapq
        m = len(mat)
        n = len(mat[0])
        for i in range(m+n-1):
            if i < m:
                r,c = i,0
            else:
                r,c = 0,i-m+1

            heap = []
            x,y = r,c
            while x < m and y < n:
                heapq.heappush(heap,mat[x][y])
                x += 1
                y += 1
            x,y = r,c
            while x < m and y < n:
                mat[x][y] = heapq.heappop(heap)
                x += 1
                y += 1
        return mat

    def diagonalSort_countsort(self, mat: List[List[int]]) -> List[List[int]]:
        """
            passing by assignment. use list.clear() instead of re-assignment
        """
        def countingSort(nums,minValue,maxValue):
            c = Counter(nums)
            nums.clear()
            for i in range(maxValue,minValue-1,-1):
                nums.extend([i]*c[i])


        from collections import defaultdict,Counter
        diags = defaultdict(list)
        
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                diags[i-j].append(mat[i][j])

        for d in diags:
            countingSort(diags[d],1,100)
        for i in range(m):
            for j in range(n):
                mat[i][j] = diags[i-j].pop()

        return mat

    def diagonalSort_countsort_2(self, mat: List[List[int]]) -> List[List[int]]:
        """
            passing by assignment. use list.clear() instead of re-assignment
        """
        def countingSort(nums):
            c = Counter(nums)
            nums.clear()
            for i in sorted(c,reverse = True):
                nums.extend([i]*c[i])


        from collections import defaultdict,Counter
        diags = defaultdict(list)
        
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                diags[i-j].append(mat[i][j])

        for d in diags:
            countingSort(diags[d])
        for i in range(m):
            for j in range(n):
                mat[i][j] = diags[i-j].pop()

        return mat

s = Solution()
print(s.diagonalSort_countsort_2([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))