class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
            #quadtree
        """
        def makeTree(r1,c1,r2,c2):
            def isLeaf():
                cnt1 = cnt0 = 0
                for i in range(r1,r2):
                    for j in range(c1,c2):
                        if grid[i][j] == 1:
                            cnt1 += 1
                        else:
                            cnt0 +=1
                        if cnt1 and cnt0:
                            return False
                return True
            
            if r1 == r2 and c1 == c2:
                return None
            elif isLeaf():
                return Node(grid[r1][c1],1)
            else:
                r3 = (r1+r2)//2
                c3 = (c1+c2)//2
                return Node(1,0,makeTree(r1,c1,r3,c3),makeTree(r1,c3,r3,c2),makeTree(r3,c1,r2,c3),makeTree(r3,c3,r2,c2))
        n = len(grid)
        return makeTree(0,0,n,n)