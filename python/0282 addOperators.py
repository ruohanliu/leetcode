class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
            #dfs #important
            related 224 227
        """
        def dfs(i, path, value, last):
            nonlocal ans
            if i == n and value == target:
                ans.append(path)
            
            for j in range(i + 1, n + 1):
                operand = int(num[i: j])
                if j == i + 1 or num[i] != "0":
                    if last is None :
                        dfs(j, num[i: j], operand, operand)
                    else:
                        dfs(j, path + '+' + num[i: j], value + operand, operand)
                        dfs(j, path + '-' + num[i: j], value - operand, -operand)
                        dfs(j, path + '*' + num[i: j], value - last + last*operand, last*operand)
        
        ans, n = [], len(num)
        dfs(0, "", 0, None)
        return ans