from typing import List
from collections import defaultdict
class Solution:
    def ladderLength_tle(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            #bfs
            Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
        """
        def match(s1,s2):
            return sum(s1[i]!=s2[i] for i in range(len(s1))) == 1
        
        cnt = 1
        curr = [beginWord]
        words = set(wordList)
        if endWord not in words:
            return 0
        while words and curr:
            next = []
            for s1 in curr:
                usedWords = set()
                for s2 in words:
                    if s2 not in usedWords:
                        if match(s1,s2):
                            if s2 == endWord:
                                return cnt+1
                            next.append(s2)
                            usedWords.add(s2)
                words-=usedWords
            cnt +=1
            curr = next
        return 0
        
    def ladderLength_tle(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            #bfs
        """
        if endWord not in wordList:
            return 0
        
        n = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(n):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        cnt = 1
        while queue:
            for _ in range(len(queue)):
                s1 = queue.popleft()
                for i in range(n):
                    s1i = s1[:i] + "*" + s1[i+1:]
                    for s2 in all_combo_dict[s1i]:
                        if s2 == endWord:
                            return cnt +1
                        
                        if s2 not in visited:
                            queue.append(s2)
                            visited.add(s2)
                    all_combo_dict[s1i] = []
            cnt +=1
        return 0