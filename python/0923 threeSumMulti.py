class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        c = Counter(arr)
        ans = 0
        sortedKey = sorted(c)
        n = len(sortedKey)
        mod = 10**9+7
        for i,x in enumerate(sortedKey):
            if 3*x>target:
                break
            if 3*x == target:
                if c[x] > 2:
                    ans = (ans + c[x]*(c[x]-1)*(c[x]-2)//6) % mod
            else:
                if c[x]>1 and c[target-2*x] > 0:
                    ans = (ans + c[x]*(c[x]-1)//2*c[target-2*x] ) % mod
                if (target - x) % 2 == 0 and c[(target-x)//2] > 1:
                    ans = (ans + c[x]*(c[(target-x)//2]-1)*c[(target-x)//2]//2) % mod
            lo = i+1
            hi = n-1
            while lo < hi:
                if sortedKey[lo] + sortedKey[hi] < target-x:
                    lo+=1
                elif sortedKey[lo] + sortedKey[hi] > target-x:
                    hi -= 1
                else:
                    ans = (ans + c[sortedKey[lo]] * c[sortedKey[hi]] * c[x]) % mod
                    lo+=1
                    hi -= 1
        return ans