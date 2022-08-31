class Solution:
    def maxProfit(self, A: List[int], orders: int) -> int:
        """
            #greedy
            related 2333
        """
        mod = 10**9+7                
        n = len(A)
        A.sort(reverse = True)
        A.append(0)
        w = 1
        ans = 0
        h = A[0]
        for i in range(n):
            if A[i+1] < A[i]:
                if w*(A[i] - A[i+1]) < orders:
                    orders -= w*(A[i] - A[i+1])
                    ans = (ans + w*(h+A[i+1]+1)*(h-A[i+1])//2) % mod
                    h = A[i+1]
                else:
                    level,m = divmod(orders,w)
                    orders -= level*w
                    ans = (ans + w*(h+h-level+1)*level//2) % mod
                    ans = (ans + (h-level)*orders) %mod
                    return ans
            w += 1