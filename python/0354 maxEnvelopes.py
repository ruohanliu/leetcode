class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
            #lis
            related 300
        """
        n = len(envelopes)
        envelopes.sort(key = lambda x:(x[0],-x[1]))
        lis = [envelopes[0][1]]
        for i in range(1,n):
            if envelopes[i][1] > lis[-1]:
                lis.append(envelopes[i][1])
            else:
                lis[bisect.bisect_left(lis,envelopes[i][1])] = envelopes[i][1]
        return len(lis)