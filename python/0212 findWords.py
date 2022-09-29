class Trie:
    def __init__(self,parent = None,val = ""):
        self.nodes = {}
        self.end = False
        self.parent = parent
        self.val = val
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(i,j,node,chars):
            nonlocal ans
            char = board[i][j]
            if char in node.nodes:
                board[i][j] = ""
                chars.append(char)
                node = node.nodes[char]
                if node.end:
                    ans.add("".join(chars))
                    node.end = False
                    curr = node
                    while not curr.nodes and not curr.end:
                        val = curr.val
                        curr = curr.parent
                        if not curr:
                            break
                        del curr.nodes[val]
                    
                for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                    r = i+di
                    c = j+dj
                    if m>r>=0<=c<n:
                        backtrack(r,c,node,chars)
                node = node.parent
                board[i][j] = char
                chars.pop()
            else:
                return

        trie = Trie()
        for word in words:
            node = trie
            for c in word:
                if c not in node.nodes:
                    node.nodes[c] = Trie(parent = node,val = c)
                node = node.nodes[c]
            node.end = True
        m = len(board)
        n = len(board[0])
        ans = set()
        for i in range(m):
            for j in range(n):
                backtrack(i,j,trie,[])
        return list(ans)