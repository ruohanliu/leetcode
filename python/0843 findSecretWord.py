class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        """
            #google

            O(n^2)
        """
        def similarity(s1,s2):
            return sum(s1[i] == s2[i] for i in range(len(s1)))

        n = len(words)
        scores = [[0] * n for _ in range(n)]
        sortedWords = [0] * n
        for i in range(n-1):
            for j in range(i+1,n):
                score = similarity(words[i],words[j])
                sortedWords[i] += score
                sortedWords[j] += score
                scores[i][j] = score
        sortedWords = sorted([(x,i) for i,x in enumerate(sortedWords)])
        visited = [False] * n
        
        while sortedWords:
            _,i = sortedWords.pop()
            if not visited[i]:
                candidate = words[i]
                target = master.guess(candidate)
                for j in range(n):
                    if (j > i and scores[i][j] != target) or (j < i and scores[j][i] != target):
                        visited[j] = True

    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        """
            O(n)
        """
        weights = [Counter(word[i] for word in words) for i in range(6)]
        sortedWords = sorted(words,key=lambda word: sum(weights[i][c] for i, c in enumerate(word)))
        
        while sortedWords:
            word = sortedWords.pop()
            target  = master.guess(word)
            sortedWords = [other for other in sortedWords if target == sum(w == o for w, o in zip(word, other))]
