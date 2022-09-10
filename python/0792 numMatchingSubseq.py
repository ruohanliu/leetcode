class Solution:
    def numMatchingSubseq(self, S, words):
        """
            #iter #important #subsequence #google #databricks

            successfully matched word will have None has key in wordsIter

            Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
        """
        wordsIter = defaultdict(list)
        for it in map(iter,words):
            wordsIter[next(it)]+=it,
        for c in S:
            for it in wordsIter.pop(c,[]):
                wordsIter[next(it,None)]+=it,
        return len(wordsIter[None])