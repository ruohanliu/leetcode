from typing import List
class Solution:
    def minMutation(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            #bfs

            related: 127 Word Ladder
            Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.
        """
        if endWord not in wordList:
            return -1
        
        n = len(beginWord)
        bank = set(wordList)
        visited = set([beginWord])
        queue = [beginWord]
        cnt = 0
        while queue:
            cnt += 1
            size = len(queue)
            for i in range(size):
                gene = queue.pop()
                for i in range(n):
                    for change in ("A","C","G","T"):
                        if change != gene[i]:
                            temp = gene[:i]+change+gene[i+1:]
                            if temp == endWord:
                                return cnt
                            if temp in bank and temp not in visited:
                                queue.append(temp)
                                visited.add(temp)
        return -1
        