class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        dpl = [1] * n
        dpr = [1] * n
        
        for i in range(1,n):
            if ratings[i-1]<ratings[i]:
                dpl[i] = dpl[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i+1]<ratings[i]:
                dpr[i] = dpr[i+1]+1
        ans = 0
        for i in range(n):
            ans += max(dpl[i],dpr[i])
        return ans

    def candy(self, ratings: List[int]) -> int:
        """
            related: 1632
        """
        n = len(ratings)
        items = defaultdict(list)
        ans = [0] * n
        for i,x in enumerate(ratings):
            items[x].append(i)
        
        for val in sorted(items):
            temp = defaultdict(lambda:1)
            for i in items[val]:
                if i and ratings[i-1] < val:
                    temp[i] = max(temp[i],ans[i-1]+1)
                if i<n-1 and ratings[i+1] < val:
                    temp[i] = max(temp[i],ans[i+1]+1)
                
            for i in items[val]:
                ans[i] = temp[i]
        return sum(ans)

    def candy(self, ratings: List[int]) -> int:
        up = 1
        down = 0
        ans = 1
        #relative peak height
        peak = 0

        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                up+=1
                peak = up
                down =  0
                ans+=up
            elif ratings[i]==ratings[i-1]:
                down = 0
                peak = 0
                up = 1
                ans+=up
            else:
                down+=1
                up = 1
                # compensate previous higher rating
                ans+=down
                # if descending below previous peak
                if peak<=down:
                    ans+=1
        return ans
