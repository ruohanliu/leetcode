from typing import List
from collections import Counter, defaultdict

class TrieNode:
    def __init__(self,parent = None,c=""):
        self.children = {}
        self.parent = parent
        self.ends = False
        self.c = c

class Solution:
    def findWords_trie(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
            #backtrack #dfs #trie #important

            Given an m x n board of characters and a list of strings words, return all words on the board.
        """
        def dfs(i,j,node):
            c = board[i][j]
            if c in node.children:
                node = node.children[c]
                if node.ends:
                    node.ends = False
                    curr = node
                    word = []
                    while curr:
                        word.append(curr.c)
                        curr = curr.parent
                    ans.append("".join(word[::-1]))
                    if not node.children:
                        node = node.parent
                        del node.children[c]
                        return
            else:
                return
            
            board[i][j] = "#"
            for di,dj in directions:
                ni = i+di
                nj = j+dj
                if ni < m and ni >= 0 and nj >=0 and nj < n and board[ni][nj] != "#":
                    dfs(ni,nj,node)

            board[i][j] = c
            node = node.parent

        m = len(board)
        n = len(board[0])
        directions = {(-1,0),(1,0),(0,1),(0,-1)}
        trie = TrieNode()
        ans = []

        for word in words:
            node = trie
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode(node,c)
                node = node.children[c]
            node.ends = True
        for i in range(m):
            for j in range(n):
                dfs(i,j,trie)

        return ans

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        directions = {(-1,0),(1,0),(0,1),(0,-1)}
        boardChars = Counter()
        wordDict = defaultdict(set)
        for row in board:
            boardChars.update(row)
        for word in words:
            if not (Counter(word) - boardChars):
                wordDict[word[-1]].add(word)
        foundWords = set()
        visited = set()
        ans = []

        def dfs(i,j,p,word):
            if board[i][j] == word[p]:
                p += 1
                if p == len(word):
                    return True
            else:
                return False

            visited.add((i,j))

            result = False 
            for di,dj in directions:
                ni = i+di
                nj = j+dj
                if ni < m and ni >= 0 and nj >=0 and nj < n and (ni,nj) not in visited:
                    if (word[:p]+board[ni][nj])[::-1] in wordDict[word[0]]:
                        foundWords.add((word[:p]+board[ni][nj])[::-1])
                    result |= dfs(ni,nj,p,word)

            visited.discard((i,j))
            return result
                    
        for i in range(m):
            for j in range(n):
                for word in wordDict[board[i][j]]:
                    if word not in foundWords:
                        if dfs(i,j,0,word[::-1]):
                            foundWords.add(word)
                        visited.clear()
                ans += list(foundWords)
                wordDict[board[i][j]] -= foundWords
                foundWords.clear()

        return ans
