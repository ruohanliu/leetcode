class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
            #nqueen #backtrack
        """
        def backtrack(n,i,progress):
            if i==n:
                ans.append(progress[::])
                return
            for j in range(n):
                valid = True
                for k,row in enumerate(progress):
                    if row[j] == "Q" or (0<= k-i+j < n and row[k-i+j] == "Q") or (0<= i+j-k < n and row[i+j-k] == "Q"):
                        valid = False
                        break
                if valid:
                    progress.append("."*j+"Q"+"."*(n-j-1))
                    backtrack(n,i+1,progress)
                    progress.pop()


        ans = []
        backtrack(n,0,[])

        return ans

        def backtrack(n,i,progress,col,diag,anti):
            if i==n:
                ans.append(progress[::])
                return
            for j in range(n):
                if j not in col and i-j not in diag and i+j not in anti:
                    progress.append("."*j+"Q"+"."*(n-j-1))
                    col.add(j)
                    diag.add(i-j)
                    anti.add(i+j)
                    backtrack(n,i+1,progress,col,diag,anti)
                    col.remove(j)
                    diag.remove(i-j)
                    anti.remove(i+j)
                    progress.pop()


        ans = []
        backtrack(n,0,[],set(),set(),set())

        return ans