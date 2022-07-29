class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
            #dp #lcs

            equivalent of finding longest common subsequence betwee s1 and s2

            Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.
        """
        if len(str1) < len(str2):
            str1,str2 = str2,str1
        m = len(str1)
        n = len(str2)

        prev = [[]] * (n+1)
        curr = [[]] * (n+1)
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    curr[j+1] = prev[j]+[str1[i]]
                else:
                    curr[j+1] = prev[j+1] if len(prev[j+1]) > len(curr[j]) else curr[j]
            prev,curr = curr,prev
        matched = prev[-1]
        l = len(matched)
        ans = []
        i = j = k = 0
        while i < m or j < n:
            if k == l:
                ans.extend(str1[i:]+str2[j:])
                break
            elif i == m:
                ans.extend(str2[j:])
                break
            elif j == n:
                ans.extend(str1[i:])
                break
            elif str1[i] == str2[j] == matched[k]:
                ans.append(str1[i])
                i += 1
                j += 1
                k += 1
            else:
                if str1[i] != matched[k]:
                    ans.append(str1[i])
                    i += 1
                if str2[j] != matched[k]:
                    ans.append(str2[j])
                    j += 1
        return "".join(ans)