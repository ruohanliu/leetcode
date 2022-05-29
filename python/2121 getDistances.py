from typing import List
class Solution:
    def getDistances_naive(self, arr: List[int]) -> List[int]:
        """
            Time Limit Exceeded
        """
        ans = [0] * len(arr)
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i] == arr[j]:
                    ans[i] += j - i
                    ans[j] += j - i

        return ans

    def getDistances(self, arr: List[int]) -> List[int]:
        """
            #math
            use dict {key:[indices]} to group and store indices of the same number
            one pass the dict indices to compute sum of indices at each location
            indices are sorted naturally, therefore later index - earlier index is positive

            k1-k1 + k2-k1 +... km-k1 = f(1) 
            k2-k1 + k2-k2 +...km -k2 = f(2) 
            k3-k1 + k3-k2 +...km -k3 = f(3)

            delta = indices[i] - indices[i-1]
            f(i) = f(i-1) - delta * (m - i) + i * delta

            take away:
                sum cannot be used as var name
        """
        from collections import defaultdict
        dict = defaultdict(list)
        n = len(arr)
        ans = [0] * n
        for i,num in enumerate(arr):
            dict[num].append(i)
        for indices in dict.values():
            m = len(indices)
            # f(0)
            index_diff_sum = sum(indices) - indices[0] * m
            for i,index in enumerate(indices):
                delta = indices[i] - indices[i-1] if i>= 1 else 0
                # f(i)
                index_diff_sum += i * delta - (m - i) * delta
                ans[index] = index_diff_sum
        return ans

s = Solution()
print(s.getDistances([2,1,3,1,2,3,3]))
