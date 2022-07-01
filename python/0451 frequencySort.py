class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        res = []
        for k in sorted(c.keys(),key = lambda x: -c[x]):
            res.extend([k] * c[k])
        return "".join(res)

    def frequencySort(self, s: str) -> str:
        """
            #bucketsort #algorithm 
            O(N): good for low amount of bucket, and not distinguishing values in the same bucket
        """

        if not s: return s
        
        # Determine the frequency of each character.
        counts = collections.Counter(s)
        max_freq = max(counts.values())
        
        # Bucket sort the characters by frequency.
        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            buckets[i].append(c)
            
        # Build up the string.
        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)
                
        return "".join(string_builder)
