class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
            #slidingwindow #important
            same as 159 related 340 992 
            longest subarray with k distinct element
        """
        ans = 0
        a = -1
        b = -1
        count_ab = 0
        count_b = 0
        for c in fruits:
            count_ab = count_ab + 1 if c in (a,b) else count_b + 1
            count_b = count_b + 1 if c == b else 1
            if b != c:
                a,b = b,c
            ans = max(ans,count_ab)
        return ans

    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        i = 0
        for j,f in enumerate(fruits):
            count[f] += 1
            if len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
        return j-i+1