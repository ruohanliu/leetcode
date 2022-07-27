class Solution:
    def pathSum(self, nums: List[int]) -> int:
        """
            #contribution
        """
        cnt = defaultdict(int)
        ans = 0
        lastDepth = 5
        for num in reversed(nums):
            depth,pos,val = num//100,num//10%10-1,num%10
            if depth<lastDepth:
                _cnt = defaultdict(int)
                for x in cnt:
                    _cnt[x//2] += cnt[x]
                cnt = _cnt
                lastDepth = depth
            if pos not in cnt:
                cnt[pos] = 1
            ans += val * cnt[pos]
        return ans
            